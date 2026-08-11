# @ohos.app.ability.dialogRequest

The dialogRequest module provides APIs related to modal dialog box processing, including obtaining the request information (used to bind a modal dialog box) and request callback (used to set the request result).

A modal dialog box is a system-level dialog box that blocks interactions such as mouse clicks, keyboard input, and touch events on the underlying page. The page can only be interacted with after the modal dialog box is closed.

> **NOTE：**
> 
> - The APIs provided by this module are used in ServiceExtensionAbilities. For a ServiceExtensionAbility that
> implements modal dialog boxes, you can use the APIs to obtain the request information and request callback and
> return the request result.

**Since:** 9

<!--Device-unnamed-declare namespace dialogRequest--><!--Device-unnamed-declare namespace dialogRequest-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { dialogRequest } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getRequestCallback](arkts-ability-dialogrequest-getrequestcallback-f.md#getrequestcallback) |
| [getRequestInfo](arkts-ability-dialogrequest-getrequestinfo-f.md#getrequestinfo) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [RequestCallback](arkts-ability-dialogrequest-requestcallback-i.md) |
| [RequestInfo](arkts-ability-dialogrequest-requestinfo-i.md) |
| [RequestResult](arkts-ability-dialogrequest-requestresult-i.md) |
| [WindowRect](arkts-ability-dialogrequest-windowrect-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ResultCode](arkts-ability-dialogrequest-resultcode-e.md) |
