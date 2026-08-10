# Provider

Defining Provider annotation Provider is used for two-way data synchronization with descendant components when state data needs to be transferred between multiple levels. An @Provider decorated state variable exists in the ancestor component and is said to be "provider" to descendent components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare @interface Provider--><!--Device-unnamed-export declare @interface Provider-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alias

```TypeScript
alias: string = ""
```

用于设置别名，默认值为属性名。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Provider-alias: string = ""--><!--Device-Provider-alias: string = ""-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

