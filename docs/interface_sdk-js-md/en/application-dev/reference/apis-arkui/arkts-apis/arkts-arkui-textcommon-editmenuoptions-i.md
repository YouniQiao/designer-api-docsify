# EditMenuOptions

EditMenuOptions

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onPrepareMenu

```TypeScript
onPrepareMenu?: OnPrepareMenuCallback
```

Callback before displaying the menu when the selection range changes.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onCreateMenu

```TypeScript
onCreateMenu: OnCreateMenuCallback | undefined
```

Passes the default menu, invokes before every display to generate a menu for triggering click events. If `undefined` is passed, the existing registered event will be removed.

**Type:** [OnCreateMenuCallback](arkts-arkui-oncreatemenucallback-t.md) \| undefined

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## onMenuItemClick

```TypeScript
onMenuItemClick: OnMenuItemClickCallback | undefined
```

Invoke upon clicking an item, capable of intercepting the default system menu execution behavior. If `undefined` is passed, the existing registered event will be removed.

**Type:** [OnMenuItemClickCallback](arkts-arkui-onmenuitemclickcallback-t.md) \| undefined

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
