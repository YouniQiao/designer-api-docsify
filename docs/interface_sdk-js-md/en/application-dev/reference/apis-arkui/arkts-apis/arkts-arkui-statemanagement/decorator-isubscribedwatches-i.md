# ISubscribedWatches

Define ISubscribedWatches interface.

**Inheritance/Implementation:** ISubscribedWatches extends [IWatchSubscriberRegister](decorator-iwatchsubscriberregister-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ISubscribedWatches extends IWatchSubscriberRegister--><!--Device-unnamed-export declare interface ISubscribedWatches extends IWatchSubscriberRegister-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## executeOnSubscribingWatches

```TypeScript
executeOnSubscribingWatches(propertyName: string): void
```

Execute the watch function callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ISubscribedWatches-executeOnSubscribingWatches(propertyName: string): void--><!--Device-ISubscribedWatches-executeOnSubscribingWatches(propertyName: string): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| propertyName | string | Yes | property name |

