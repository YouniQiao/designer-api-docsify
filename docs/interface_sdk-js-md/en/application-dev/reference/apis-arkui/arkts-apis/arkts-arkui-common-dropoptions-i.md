# DropOptions

Defines the options for the drop handling.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## disableDataPrefetch

```TypeScript
disableDataPrefetch?: boolean
```

Indicating to disable the UDMF data prefetch action by system or not. The system will try to fetch data before calling user's onDrop for some situation, it will retry to get data until the max time limit (2.4s for now) reaches, this's useful for the cross device draging operation, as the system helps to eliminate the communication instability, but it's redundant for startDataLoading method, as this method will take care the data fetching with asynchronous mechanism, so must set this field to true if using startDataLoading in onDrop to avoid the data is fetched before onDrop executing unexpectedly.

**Type:** boolean

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
