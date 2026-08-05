# WindowChangeOptions

Describes the extended configuration of window change event listening, which is used to specify the listening process configuration and event filtering conditions.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

<!--Device-unnamed-declare interface WindowChangeOptions--><!--Device-unnamed-declare interface WindowChangeOptions-End-->

**System capability:** SystemCapability.Test.UiTest

## bundleName

```TypeScript
bundleName?: string
```

Bundle name of the window to be listened for. By default, all windows are listened for.

**Type:** string

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-WindowChangeOptions-bundleName?: string--><!--Device-WindowChangeOptions-bundleName?: string-End-->

**System capability:** SystemCapability.Test.UiTest

## timeout

```TypeScript
timeout?: int
```

Listening timeout interval, to prevent listening failures casued by event notification delay. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Value range: The value should be >= 500 \_\_\_HTML\_TAG\_DESC\_USD\_1\_\_\_Default value: 10000 \_\_\_HTML\_TAG\_DESC\_USD\_2\_\_\_Unit: ms

**Type:** int

**Since:** 22

**ArkTS mode:** ArkTS-Dyn since version 22; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-WindowChangeOptions-timeout?: int--><!--Device-WindowChangeOptions-timeout?: int-End-->

**System capability:** SystemCapability.Test.UiTest

