# SyncMonitor

Define SyncMonitor MethodDecorator. Decorator path parameters are the same as defined for Monitor.The function decorator is functionally equivalent to the UIUtils.addMonitor API with isSynchronous enabled.SyncMonitor must contain at least one path item, with multiple path items separated by commas.Path items are either observed attribute names or array item indices.The path in SyncMonitor supports wildcard at the end of a path item, but path items must never appear at the beginning or in the middle of a path. All other paths using one or more wildcard are invalid.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export declare @interface SyncMonitor--><!--Device-unnamed-export declare @interface SyncMonitor-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string[]
```

监听V2状态变量变量名

**类型：** string[]

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SyncMonitor-path: string[]--><!--Device-SyncMonitor-path: string[]-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

