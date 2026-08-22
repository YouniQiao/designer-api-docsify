# MonitorOptions

Define Monitor options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface MonitorOptions--><!--Device-unnamed-export declare interface MonitorOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSynchronous

```TypeScript
isSynchronous?: boolean
```

Used to determine whether the state variable change is triggered synchronously or asynchronously. The default value is false.

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorOptions-isSynchronous?: boolean--><!--Device-MonitorOptions-isSynchronous?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## owner

```TypeScript
owner?: IVariableOwner
```

Used to handle component freezing. If not set, component freezing won't affect the monitor.

**Type:** [IVariableOwner](arkts-decorator-ivariableowner-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorOptions-owner?: IVariableOwner--><!--Device-MonitorOptions-owner?: IVariableOwner-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path?: string | string[]
```

Override path for each valueCallback element.

**Type:** string \| string[]

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorOptions-path?: string | string[]--><!--Device-MonitorOptions-path?: string | string[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

