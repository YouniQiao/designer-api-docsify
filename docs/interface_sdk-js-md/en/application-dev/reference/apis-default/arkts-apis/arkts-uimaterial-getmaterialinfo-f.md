# getMaterialInfo

## Modules to Import

```TypeScript
```

## getMaterialInfo

```TypeScript
export function getMaterialInfo(): MaterialInfo
```

Obtains the material configuration information of this application. The returned configuration information comes from the metadata configured in the [module.json5](../../../quick-start/module-configuration-file.md) file of the application.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-uiMaterial-export function getMaterialInfo(): MaterialInfo--><!--Device-uiMaterial-export function getMaterialInfo(): MaterialInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MaterialInfo](arkts-uimaterial-materialinfo-i.md) | Material configuration information of this application, including the material enabling state and material type. |

