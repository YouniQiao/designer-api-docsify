# KeyEventPolicy

按键事件处理策略。按键事件发生时，仅拦截响应已下发按键事件处理策略的按键。对于未下发按键事件处理策略的按键事件，系统执行原先的响应逻辑。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-systemManager-interface KeyEventPolicy--><!--Device-systemManager-interface KeyEventPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## keyCode

```TypeScript
keyCode: KeyCode
```

按键编码。

**Type:** [KeyCode](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keycode-keycode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEventPolicy-keyCode: KeyCode--><!--Device-KeyEventPolicy-keyCode: KeyCode-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## keyPolicy

```TypeScript
keyPolicy: KeyPolicy
```

按键策略。

**Type:** [KeyPolicy](arkts-mdm-systemmanager-keypolicy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-KeyEventPolicy-keyPolicy: KeyPolicy--><!--Device-KeyEventPolicy-keyPolicy: KeyPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

