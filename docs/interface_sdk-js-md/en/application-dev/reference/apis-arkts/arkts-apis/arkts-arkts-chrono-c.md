# Chrono

Utility class for time measurement and clock access.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

<!--Device-unnamed-export class Chrono--><!--Device-unnamed-export class Chrono-End-->

**System capability:** SystemCapability.Utils.Lang

## Modules to Import

```TypeScript
```

## getCpuTime

```TypeScript
public static getCpuTime(): long
```

Gets the current process CPU time in nanoseconds.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Chrono-public static getCpuTime(): long--><!--Device-Chrono-public static getCpuTime(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | the CPU time in nanoseconds consumed by the current process. |

## milliNow

```TypeScript
public static milliNow(): double
```

Gets the current timestamp in milliseconds.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Chrono-public static milliNow(): double--><!--Device-Chrono-public static milliNow(): double-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| double | the number of milliseconds elapsed since system start. |

## nanoNow

```TypeScript
public static nanoNow(): long
```

Gets the current timestamp in nanoseconds.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Chrono-public static nanoNow(): long--><!--Device-Chrono-public static nanoNow(): long-End-->

**System capability:** SystemCapability.Utils.Lang

**Return value:**

| Type | Description |
| --- | --- |
| long | the number of nanoseconds elapsed since system start. |

## NS_PER_MS

```TypeScript
public static readonly NS_PER_MS: long = 1000000
```

The number of nanoseconds in one millisecond.

**Type:** long

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Chrono-public static readonly NS_PER_MS: long = 1000000--><!--Device-Chrono-public static readonly NS_PER_MS: long = 1000000-End-->

**System capability:** SystemCapability.Utils.Lang

