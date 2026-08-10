# DropOptions

设置落入过程的参数。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-unnamed-declare interface DropOptions--><!--Device-unnamed-declare interface DropOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableDataPrefetch

```TypeScript
disableDataPrefetch?: boolean
```

设置拖拽是否提前获取数据。true表示不提前获取数据，false表示提前获取数据，默认值为false。

**说明：**

当使用[startDataLoading](arkts-arkui-dragevent-i.md#startdataloading)获取数据时需设置该参数为true，防止拖拽提前获取数据。

**Type:** boolean

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-DropOptions-disableDataPrefetch?: boolean--><!--Device-DropOptions-disableDataPrefetch?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

