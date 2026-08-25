# @ohos.app.ability.autoFillManager

The autoFillManager module provides APIs for saving accounts and passwords.Unlike the system's auto-save feature that triggers during page transitions, this feature requires manual activation by the user. For example, the user must input their account and password on a website and click the **Save** button to initiate the saving process.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { autoFillManager } from 'kits/@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [requestAutoFill](arkts-ability-autofillmanager-requestautofill-f.md) |
| [requestAutoSave](arkts-ability-autofillmanager-requestautosave-f.md) |
| [requestAutoSave](arkts-ability-autofillmanager-requestautosave-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AutoFillCallback](arkts-ability-autofillmanager-autofillcallback-i.md) |
| [AutoSaveCallback](arkts-ability-autofillmanager-autosavecallback-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AutoFillRect](arkts-ability-autofillmanager-autofillrect-t.md) |
| [FillFailureResult](arkts-ability-autofillmanager-fillfailureresult-t.md) |
| [FillRequest](arkts-ability-autofillmanager-fillrequest-t.md) |
| [OnFillFailureFn](arkts-ability-autofillmanager-onfillfailurefn-t.md) |
| [OnFillSuccessFn](arkts-ability-autofillmanager-onfillsuccessfn-t.md) |
| [PageNodeInfo](arkts-ability-autofillmanager-pagenodeinfo-t.md) |
| [SaveRequest](arkts-ability-autofillmanager-saverequest-t.md) |
| [ViewData](arkts-ability-autofillmanager-viewdata-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AutoFillPopupConfig](arkts-ability-autofillmanager-autofillpopupconfig-t-sys.md) |
| [CustomData](arkts-ability-autofillmanager-customdata-t-sys.md) |
| [FillRequestCallback](arkts-ability-autofillmanager-fillrequestcallback-t-sys.md) |
| [FillResponse](arkts-ability-autofillmanager-fillresponse-t-sys.md) |
| [PopupSize](arkts-ability-autofillmanager-popupsize-t-sys.md) |
| [SaveRequestCallback](arkts-ability-autofillmanager-saverequestcallback-t-sys.md) |
| [UpdateRequest](arkts-ability-autofillmanager-updaterequest-t-sys.md) |
<!--DelEnd-->
