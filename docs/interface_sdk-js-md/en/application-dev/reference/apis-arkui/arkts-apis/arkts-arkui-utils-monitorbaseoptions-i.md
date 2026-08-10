# MonitorBaseOptions

监听基础选项。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface MonitorBaseOptions--><!--Device-unnamed-export declare interface MonitorBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSynchronous

```TypeScript
isSynchronous?: boolean
```

是否同步回调。

true：同步回调；false：异步回调。

默认值：false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorBaseOptions-isSynchronous?: boolean--><!--Device-MonitorBaseOptions-isSynchronous?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## owner

```TypeScript
owner?: IVariableOwner
```

指定冻结的组件，仅能传入[@ComponentV2](../../../ui/state-management-static/arkts-static-componentv2.md)装饰的自定义组件。默认值为`undefined`，即不指定冻结的组件。

**Type:** [IVariableOwner](arkts-arkui-decorator-ivariableowner-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorBaseOptions-owner?: IVariableOwner--><!--Device-MonitorBaseOptions-owner?: IVariableOwner-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

