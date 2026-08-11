# Material

System material object on the UI.

**Since:** 26.0.0

<!--Device-uiMaterial-class Material--><!--Device-uiMaterial-class Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { uiMaterial } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(options?: MaterialOptions)
```

A constructor used to create a **Material** object.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-Material-constructor(options?: MaterialOptions)--><!--Device-Material-constructor(options?: MaterialOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [MaterialOptions](arkts-arkui-uimaterial-materialoptions-i.md) | No |

## empty

```TypeScript
static get empty(): Material
```

Returns an empty material object, which is used to disable the immersive system material effect for a component. The usage method is **uiMaterial.Material.empty**.

In enabled state, you can disable the immersive system material effect for a component by setting   
**systemMaterial(uiMaterial.Material.empty)**. If the component does not support the component-level immersive system material API, the material effect cannot be disabled using this API.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-Material-static get empty(): Material--><!--Device-Material-static get empty(): Material-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full
