# ScrollOptions

ScrollOptions

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-unnamed-export interface ScrollOptions--><!--Device-unnamed-export interface ScrollOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## complete

```TypeScript
complete?: (result: Object) => void
```

Callback function at the end of the interface invoking (executed both successfully and unsuccessfully).

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ScrollOptions-complete?: (result: Object) => void--><!--Device-ScrollOptions-complete?: (result: Object) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | Object | 是 |  |

## fail

```TypeScript
fail?: (result: Object) => void
```

Callback function for interface invocation failure.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ScrollOptions-fail?: (result: Object) => void--><!--Device-ScrollOptions-fail?: (result: Object) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | Object | 是 |  |

## success

```TypeScript
success?: (result: Object) => void
```

Callback function for successful interface invocation.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ScrollOptions-success?: (result: Object) => void--><!--Device-ScrollOptions-success?: (result: Object) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | Object | 是 |  |

## duration

```TypeScript
duration: number
```

Duration of the scrolling animation, in ms.

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ScrollOptions-duration: number--><!--Device-ScrollOptions-duration: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id?: string
```

The selector for current scroll.

**类型：** string

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ScrollOptions-id?: string--><!--Device-ScrollOptions-id?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## position

```TypeScript
position: number
```

Scroll to the target position of the page. Unit: px

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ScrollOptions-position: number--><!--Device-ScrollOptions-position: number-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## timingFunction

```TypeScript
timingFunction?: string
```

The timing function for current scroll animation.

**类型：** string

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-ScrollOptions-timingFunction?: string--><!--Device-ScrollOptions-timingFunction?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

