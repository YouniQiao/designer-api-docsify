# Material

Base class of the system material object on the UI.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-uiMaterial-export class Material--><!--Device-uiMaterial-export class Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiMaterial } from '@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: MaterialOptions)
```

Constructor of material class.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Material-constructor(options?: MaterialOptions)--><!--Device-Material-constructor(options?: MaterialOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [MaterialOptions](arkts-arkui-uimaterial-materialoptions-i.md) | No | the options to construct a material. &lt;br&gt;Default value:{type:uiMaterial.MaterialType.NONE} |

## empty

```TypeScript
static get empty(): Material
```

Returns an empty material object, which is used to disable the immersive system material effect for a component. The usage method is **uiMaterial.Material.empty**.

In enabled state, you can disable the immersive system material effect for a component by setting   
**systemMaterial(uiMaterial.Material.empty)**. If the component does not support the component-level immersive system material API, the material effect cannot be disabled using this API.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Material-static get empty(): Material--><!--Device-Material-static get empty(): Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

