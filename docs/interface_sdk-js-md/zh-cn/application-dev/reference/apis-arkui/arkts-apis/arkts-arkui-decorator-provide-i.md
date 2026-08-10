# Provide

Defining Provide annotation Provide is used for two-way data synchronization with descendant components when state data needs to be transferred between multiple levels. An @Provide decorated state variable exists in the ancestor component and is said to be "provided" to descendent components.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare @interface Provide--><!--Device-unnamed-export declare @interface Provide-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alias

```TypeScript
alias: string = ""
```

用于设置别名，默认值为属性名。

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Provide-alias: string = ""--><!--Device-Provide-alias: string = ""-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## allowOverride

```TypeScript
allowOverride: boolean = false
```

用于设置是否允许重载，默认值为false即不允许。

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Provide-allowOverride: boolean = false--><!--Device-Provide-allowOverride: boolean = false-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

