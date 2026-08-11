# Provide

Defining Provide annotation Provide is used for two-way data synchronization with descendant components when state data needs to be transferred between multiple levels. An @Provide decorated state variable exists in the ancestor component and is said to be "provided" to descendent components.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare @interface Provide--><!--Device-unnamed-export declare @interface Provide-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alias

```TypeScript
alias: string = ""
```

The alias name.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Provide-alias: string = ""--><!--Device-Provide-alias: string = ""-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## allowOverride

```TypeScript
allowOverride: boolean = false
```

allowOverride is used to override an existing @Provide decorated variable.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Provide-allowOverride: boolean = false--><!--Device-Provide-allowOverride: boolean = false-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

