# MonitorBaseOptions

Define MonitorBaseOptions.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export declare interface MonitorBaseOptions--><!--Device-unnamed-export declare interface MonitorBaseOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## isSynchronous

```TypeScript
isSynchronous?: boolean
```

Used to determine whether the state variable change is triggered synchronously or asynchronously. The default value is false.

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorBaseOptions-isSynchronous?: boolean--><!--Device-MonitorBaseOptions-isSynchronous?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## owner

```TypeScript
owner?: IVariableOwner
```

Used to handle component freezing. If not set, component freezing won't affect the monitor.

**Type:** [IVariableOwner](arkts-decorator-ivariableowner-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MonitorBaseOptions-owner?: IVariableOwner--><!--Device-MonitorBaseOptions-owner?: IVariableOwner-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

