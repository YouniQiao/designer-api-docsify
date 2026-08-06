# ComponentEventOptions

Describes the extended configuration of component operation event listening,which is used to specify the listening process configuration and event filtering conditions.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface ComponentEventOptions--><!--Device-unnamed-declare interface ComponentEventOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## on

```TypeScript
on?: On
```

Attribute requirements of the target component to listen for. By default, all components are listened for.  
**Note**: Only components with specified attributes can be listened for. Components with relative positions such as  
**On.isBefore**, **On.isAfter**, and **On.within** cannot be listened for.

**Type:** On

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ComponentEventOptions-on?: On--><!--Device-ComponentEventOptions-on?: On-End-->

**System capability:** SystemCapability.Test.UiTest

## timeout

```TypeScript
timeout?: int
```

Listening timeout interval , to prevent listening failures casued by event notification delay.\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Value range: The value should be >= 500\_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: 10000\_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Unit: ms

**Type:** int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-ComponentEventOptions-timeout?: int--><!--Device-ComponentEventOptions-timeout?: int-End-->

**System capability:** SystemCapability.Test.UiTest

