# @ohos.app.ability.autoFillManager

The autoFillManager module provides APIs for saving accounts and passwords. Unlike the system's auto-save feature that triggers during page transitions, this feature requires manual activation by the user. For example, the user must input their account and password on a website and click the **Save** button to initiate the saving process.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace autoFillManager--><!--Device-unnamed-declare namespace autoFillManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.AbilityCore

## Modules to Import

```TypeScript
import { autoFillManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [requestAutoFill](arkts-ability-autofillmanager-requestautofill-f.md#requestAutoFill) |
| [requestAutoSave](arkts-ability-autofillmanager-requestautosave-f.md#requestAutoSave) |
| [requestAutoSave](arkts-ability-autofillmanager-requestautosave-f.md#requestAutoSave) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AutoFillCallback](arkts-ability-autofillmanager-autofillcallback-i.md) |
| [AutoSaveCallback](arkts-ability-autofillmanager-autosavecallback-i.md) |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FillFailureResult](arkts-ability-autofillmanager-fillfailureresult-t.md) |
| [OnFailureFn](arkts-ability-autofillmanager-onfailurefn-t.md) |
| [OnFillFailureFn](arkts-ability-autofillmanager-onfillfailurefn-t.md) |
| [OnFillSuccessFn](arkts-ability-autofillmanager-onfillsuccessfn-t.md) |
| [OnSuccessFn](arkts-ability-autofillmanager-onsuccessfn-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AutoFillPopupConfig](arkts-ability-autofillmanager-autofillpopupconfig-t-sys.md) |
| [AutoFillRect](arkts-ability-autofillmanager-autofillrect-t-sys.md) |
| [AutoFillTriggerType](arkts-ability-autofillmanager-autofilltriggertype-t-sys.md) |
| [AutoFillType](arkts-ability-autofillmanager-autofilltype-t-sys.md) |
| [CustomData](arkts-ability-autofillmanager-customdata-t-sys.md) |
| [FillRequest](arkts-ability-autofillmanager-fillrequest-t-sys.md) |
| [FillRequestCallback](arkts-ability-autofillmanager-fillrequestcallback-t-sys.md) |
| [FillResponse](arkts-ability-autofillmanager-fillresponse-t-sys.md) |
| [PageNodeInfo](arkts-ability-autofillmanager-pagenodeinfo-t-sys.md) |
| [PopupPlacement](arkts-ability-autofillmanager-popupplacement-t-sys.md) |
| [PopupSize](arkts-ability-autofillmanager-popupsize-t-sys.md) |
| [SaveRequest](arkts-ability-autofillmanager-saverequest-t-sys.md) |
| [SaveRequestCallback](arkts-ability-autofillmanager-saverequestcallback-t-sys.md) |
| [UpdateRequest](arkts-ability-autofillmanager-updaterequest-t-sys.md) |
| [ViewData](arkts-ability-autofillmanager-viewdata-t-sys.md) |
<!--DelEnd-->
