# MonitorOptions

设置监听的行为。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface MonitorOptions--><!--Device-unnamed-export declare interface MonitorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSynchronous

```TypeScript
isSynchronous?: boolean
```

指定函数是否同步执行，`true`为同步，`false`为异步。默认为`false`。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorOptions-isSynchronous?: boolean--><!--Device-MonitorOptions-isSynchronous?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## owner

```TypeScript
owner?: IVariableOwner
```

指定冻结的组件，仅能传入@ComponentV2装饰的自定义组件，默认值为`undefined`。

**Type:** [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorOptions-owner?: IVariableOwner--><!--Device-MonitorOptions-owner?: IVariableOwner-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path?: string | string[]
```

显式指定监听状态变量的路径，默认为`addMonitor`自动生成的路径。

**Type:** string \| string[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorOptions-path?: string | string[]--><!--Device-MonitorOptions-path?: string | string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

