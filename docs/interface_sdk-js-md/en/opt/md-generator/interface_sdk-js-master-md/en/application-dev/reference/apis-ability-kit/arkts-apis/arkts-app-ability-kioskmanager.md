# @ohos.app.ability.kioskManager

The KioskManager module provides APIs to manage kiosk mode, including entering/exiting kiosk mode and querying the kiosk mode status.

Kiosk mode is a dedicated device lockdown mode that ensures the device UI serves only specific interaction scenarios.In this mode, device usage is confined to predetermined applications. A typical example is a bank ATM, where users can only interact with the ATM software and cannot exit it or access any other functions.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace kioskManager--><!--Device-unnamed-declare namespace kioskManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { kioskManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [enterKioskMode](arkts-ability-kioskmanager-enterkioskmode-f.md#enterkioskmode) |
| [exitKioskMode](arkts-ability-kioskmanager-exitkioskmode-f.md#exitkioskmode) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getKioskStatus](arkts-ability-kioskmanager-getkioskstatus-f-sys.md#getkioskstatus) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [KioskStatus](arkts-ability-kioskmanager-kioskstatus-t.md) |
