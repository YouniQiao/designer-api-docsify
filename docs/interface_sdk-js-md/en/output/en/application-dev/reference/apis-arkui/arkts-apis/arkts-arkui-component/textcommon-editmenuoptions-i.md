# EditMenuOptions

EditMenuOptions

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface EditMenuOptions--><!--Device-unnamed-export declare interface EditMenuOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCreateMenu

```TypeScript
onCreateMenu: OnCreateMenuCallback | undefined
```

Passes the default menu, invokes before every display to generate a menu for triggering click events. If \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ is passed, the existing registered event will be removed.

**Type:** OnCreateMenuCallback \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditMenuOptions-onCreateMenu: OnCreateMenuCallback | undefined--><!--Device-EditMenuOptions-onCreateMenu: OnCreateMenuCallback | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMenuItemClick

```TypeScript
onMenuItemClick: OnMenuItemClickCallback | undefined
```

Invoke upon clicking an item, capable of intercepting the default system menu execution behavior. If \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ is passed, the existing registered event will be removed.

**Type:** OnMenuItemClickCallback \| undefined

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditMenuOptions-onMenuItemClick: OnMenuItemClickCallback | undefined--><!--Device-EditMenuOptions-onMenuItemClick: OnMenuItemClickCallback | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPrepareMenu

```TypeScript
onPrepareMenu?: OnPrepareMenuCallback
```

Callback before displaying the menu when the selection range changes.

**Type:** OnPrepareMenuCallback

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EditMenuOptions-onPrepareMenu?: OnPrepareMenuCallback--><!--Device-EditMenuOptions-onPrepareMenu?: OnPrepareMenuCallback-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

