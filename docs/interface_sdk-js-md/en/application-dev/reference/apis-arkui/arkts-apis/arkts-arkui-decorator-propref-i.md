# PropRef

Defining PropRef annotation PropRef is an annotation which is mutable. Any object property modifications made through PropRef are visible in the parent component, which is different from Prop. In order to prevent this, need to take a deep copy of the parent data.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
