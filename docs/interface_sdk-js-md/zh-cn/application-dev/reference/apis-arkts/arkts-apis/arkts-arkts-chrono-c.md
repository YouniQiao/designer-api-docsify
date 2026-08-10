# Chrono

Utility class for time measurement and clock access.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-unnamed-export class Chrono--><!--Device-unnamed-export class Chrono-End-->

**系统能力：** SystemCapability.Utils.Lang

## getCpuTime

```TypeScript
public static getCpuTime(): long
```

Gets the current process CPU time in nanoseconds.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Chrono-public static getCpuTime(): long--><!--Device-Chrono-public static getCpuTime(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the CPU time in nanoseconds consumed by the current process. |

## milliNow

```TypeScript
public static milliNow(): double
```

Gets the current timestamp in milliseconds.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Chrono-public static milliNow(): double--><!--Device-Chrono-public static milliNow(): double-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| double | the number of milliseconds elapsed since system start. |

## nanoNow

```TypeScript
public static nanoNow(): long
```

Gets the current timestamp in nanoseconds.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Chrono-public static nanoNow(): long--><!--Device-Chrono-public static nanoNow(): long-End-->

**系统能力：** SystemCapability.Utils.Lang

**返回值：**

| 类型 | 说明 |
| --- | --- |
| long | the number of nanoseconds elapsed since system start. |

## NS_PER_MS

```TypeScript
public static readonly NS_PER_MS: long = 1000000
```

The number of nanoseconds in one millisecond.

**类型：** long

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Chrono-public static readonly NS_PER_MS: long = 1000000--><!--Device-Chrono-public static readonly NS_PER_MS: long = 1000000-End-->

**系统能力：** SystemCapability.Utils.Lang

