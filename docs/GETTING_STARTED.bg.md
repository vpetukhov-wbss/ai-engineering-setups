# Бърз старт (български)

**Име:** `ai-engineering-setups`

**Description:** Reusable Claude Code engineering setups, AI agents, skills and playbooks for .NET, C#, Blazor, MAUI, architecture, testing, security and DevOps.

## Първо публикуване

1. В GitHub създай празно **Public** репозитори с горното име, без автоматично README/.gitignore/LICENSE.
2. Изтегли и разархивирай пакета. Влез в основната папка `ai-engineering-setups`.
3. Провери файловете и изпълни командите от [`GITHUB_REPOSITORY_METADATA.md`](../GITHUB_REPOSITORY_METADATA.md).
4. Провери дали GitHub Actions workflow `Validate AI setups` завършва успешно след първия push.

## Как се използва от всеки реален .NET проект

В основната папка на репозиторито със сетъпите:

```bash
# Преглед, без промени в проекта
python3 scripts/install.py --preset dotnet-maui --target /път/до/твоя/проект

# Копиране; съществуващите файлове НЕ се презаписват
python3 scripts/install.py --preset dotnet-maui --target /път/до/твоя/проект --apply
```

После отвори реалния проект в Claude Code. Полезни команди: `/maui-app-architecture`, `/maui-feature`, `/maui-blazor-hybrid`, `/maui-device-test`, `/maui-ios-release`, `/maui-android-release`, `/maui-desktop-release`.

**Важно:** допълни `CLAUDE.md` на реалния проект със специфичните му бизнес правила и контекст. Виж шаблона [`MAUI_CLAUDE_APPEND.md`](../overlays/maui-cross-platform/MAUI_CLAUDE_APPEND.md). Настройките от публичния репозитори не означават, че Claude може да публикува приложения в App Store или Google Play без нужните акаунти, подписване и одобрение.

## Платформи

- iOS/iPadOS: необходим е Mac с подходящ Xcode за build/signing.
- Android: Android SDK/JDK, емулатори и физически устройства; AAB за Google Play.
- Windows: WinUI 3, Windows build machine и MSIX или unpackaged deployment.
- macOS: Mac Catalyst, подписване и евентуална notarization.

**Проверка:** включеният скрипт валидира структурата на setup-а, но не компилира всички MAUI targets. Реалните проверки се извършват върху приложението и съответните build машини.

## Ionic Angular + Capacitor — iOS, Android и Web/PWA

```bash
python3 scripts/install.py --preset ionic-angular --target /path/to/ionic-project
python3 scripts/install.py --preset ionic-angular --target /path/to/ionic-project --apply

# Ако в същото репозитори има ASP.NET Core:
python3 scripts/install.py --preset dotnet-ionic-angular --target /path/to/fullstack-project --apply
```

Прочети `overlays/ionic-angular-capacitor/README.md` и добави указанията от `IONIC_CLAUDE_APPEND.md` в съществуващия CLAUDE.md. Това инсталира само инженерни правила, а не Ionic, Node, Xcode или Android SDK. Изграждането на Web bundle не доказва работеща native версия.
