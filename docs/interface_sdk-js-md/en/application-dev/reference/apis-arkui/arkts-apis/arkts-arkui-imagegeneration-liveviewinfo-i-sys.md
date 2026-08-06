# LiveViewInfo (System API)

Information for LiveView in AI image generation.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-imageGeneration-interface LiveViewInfo--><!--Device-imageGeneration-interface LiveViewInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## getLongTermTaskId

```TypeScript
getLongTermTaskId(): int
```

Get the long-term task ID for LiveView.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiveViewInfo-getLongTermTaskId(): int--><!--Device-LiveViewInfo-getLongTermTaskId(): int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| int | Returns the long-term task ID. |

## getWant

```TypeScript
getWant(): Want
```

Get the Want object for LiveView.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiveViewInfo-getWant(): Want--><!--Device-LiveViewInfo-getWant(): Want-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Returns the Want object. |

## isLiveViewNeeded

```TypeScript
isLiveViewNeeded(): boolean
```

Check whether LiveView is needed.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiveViewInfo-isLiveViewNeeded(): boolean--><!--Device-LiveViewInfo-isLiveViewNeeded(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns true if LiveView is needed, false otherwise. |

