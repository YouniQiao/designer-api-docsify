# IWatchSubscriberRegister

Define IWatchSubscriberRegister interface.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface IWatchSubscriberRegister--><!--Device-unnamed-export declare interface IWatchSubscriberRegister-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## addWatchSubscriber

```TypeScript
addWatchSubscriber(watchId: WatchIdType): void
```

Registers the watch function callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IWatchSubscriberRegister-addWatchSubscriber(watchId: WatchIdType): void--><!--Device-IWatchSubscriberRegister-addWatchSubscriber(watchId: WatchIdType): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| watchId | [WatchIdType](arkts-na-watchidtype-t.md) | Yes | the watch function id |

## removeWatchSubscriber

```TypeScript
removeWatchSubscriber(watchId: WatchIdType): boolean
```

UnRegister the watch function callback.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-IWatchSubscriberRegister-removeWatchSubscriber(watchId: WatchIdType): boolean--><!--Device-IWatchSubscriberRegister-removeWatchSubscriber(watchId: WatchIdType): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| watchId | [WatchIdType](arkts-na-watchidtype-t.md) | Yes | the watch function id |

**Return value:**

| Type | Description |
| --- | --- |
| boolean |  |

