# getMaterialInfo

## Modules to Import

```TypeScript
import { uiMaterial } from 'kits/@kit.ArkUI';
```

## getMaterialInfo

```TypeScript
export function getMaterialInfo(): MaterialInfo
```

获取当前应用的材质配置信息。返回的配置信息来自应用在[module.json5](../../../quick-start/module-configuration-file.md)中配置的metadata。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiMaterial-export function getMaterialInfo(): MaterialInfo--><!--Device-uiMaterial-export function getMaterialInfo(): MaterialInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md) | 返回当前应用的材质配置信息，包含材质使能状态和材质类型。 |

