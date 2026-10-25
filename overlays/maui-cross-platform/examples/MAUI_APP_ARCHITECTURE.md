# MAUI feature-folder example — illustration, not a generated application

This example documents file boundaries. It is not claimed to have been compiled. Inspect and adapt namespaces, startup, DI and package versions for the actual app.

```text
MyApp/
  Features/Orders/
    OrdersPage.xaml               # View markup and bindings
    OrdersPage.xaml.cs            # Constructor / view glue only
    OrdersViewModel.cs            # State, commands, cancellation
    OrderSummary.cs               # Local view contract when needed
  Services/
    IOrdersClient.cs              # Narrow interface for API interaction
    OrdersClient.cs               # HTTP implementation
  Platforms/
    Android/  iOS/  MacCatalyst/  Windows/
  MauiProgram.cs                  # Registrations
```

## OrdersPage.xaml

```xml
<?xml version="1.0" encoding="utf-8" ?>
<ContentPage xmlns="http://schemas.microsoft.com/dotnet/2021/maui"
             xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
             xmlns:vm="clr-namespace:MyApp.Features.Orders"
             x:Class="MyApp.Features.Orders.OrdersPage"
             x:DataType="vm:OrdersViewModel"
             Title="Orders">
    <VerticalStackLayout Padding="20" Spacing="12">
        <Button Text="Refresh"
                Command="{Binding RefreshCommand}"
                SemanticProperties.Hint="Reload the current orders" />
        <ActivityIndicator IsRunning="{Binding IsBusy}" />
        <Label Text="{Binding ErrorMessage}" />
        <CollectionView ItemsSource="{Binding Orders}">
            <CollectionView.ItemTemplate>
                <DataTemplate x:DataType="vm:OrderSummary">
                    <Label Text="{Binding DisplayName}" />
                </DataTemplate>
            </CollectionView.ItemTemplate>
        </CollectionView>
    </VerticalStackLayout>
</ContentPage>
```

## OrdersPage.xaml.cs

```csharp
namespace MyApp.Features.Orders;

public partial class OrdersPage : ContentPage
{
    public OrdersPage(OrdersViewModel viewModel)
    {
        InitializeComponent();
        BindingContext = viewModel;
    }
}
```

## OrdersViewModel.cs

```csharp
using System.Collections.ObjectModel;
using CommunityToolkit.Mvvm.ComponentModel;
using CommunityToolkit.Mvvm.Input;

namespace MyApp.Features.Orders;

public partial class OrdersViewModel : ObservableObject
{
    private readonly IOrdersClient _client;

    public OrdersViewModel(IOrdersClient client) => _client = client;

    public ObservableCollection<OrderSummary> Orders { get; } = new();

    [ObservableProperty]
    private bool isBusy;

    [ObservableProperty]
    private string? errorMessage;

    [RelayCommand(AllowConcurrentExecutions = false)]
    private async Task RefreshAsync(CancellationToken cancellationToken)
    {
        if (IsBusy) return;
        try
        {
            IsBusy = true;
            ErrorMessage = null;
            var items = await _client.GetOrdersAsync(cancellationToken);
            Orders.Clear();
            foreach (var order in items) Orders.Add(order);
        }
        catch (OperationCanceledException) when (cancellationToken.IsCancellationRequested)
        {
            // Navigation or user cancellation; not an error message.
        }
        catch (HttpRequestException)
        {
            ErrorMessage = "Orders are temporarily unavailable.";
        }
        finally
        {
            IsBusy = false;
        }
    }
}
```

## OrderSummary.cs

```csharp
namespace MyApp.Features.Orders;

public sealed record OrderSummary(string Id, string DisplayName);
```

## IOrdersClient.cs

```csharp
namespace MyApp.Features.Orders;

public interface IOrdersClient
{
    Task<IReadOnlyList<OrderSummary>> GetOrdersAsync(CancellationToken ct);
}
```

Register `OrdersViewModel`, `OrdersPage` and `IOrdersClient` deliberately in `MauiProgram.cs` (appropriate scopes/lifetimes). The example assumes this interface is useful for testing and backend boundary isolation; don't add interfaces solely for stylistic uniformity.

For a real feature, add loading/error/empty/sync UI semantics, pagination if necessary, local persistence only if required, unit tests, retry/error classification, and real-device accessibility checks. Use dispatcher/main-thread updates if completion callbacks are not on UI thread.
