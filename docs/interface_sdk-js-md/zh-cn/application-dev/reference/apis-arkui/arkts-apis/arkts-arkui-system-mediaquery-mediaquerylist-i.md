# MediaQueryList

Defines the MediaQuery list info.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export interface MediaQueryList--><!--Device-unnamed-export interface MediaQueryList-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { MediaQueryEvent, MediaQueryList } from 'kits/@kit.ArkUI';
```

## addListener

```TypeScript
addListener(callback: (event: MediaQueryEvent) => void): void
```

Adds a listening function to MediaQueryList.The listening function must be added before onShow is called, that is, added to the onInit or onReady function.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaQueryList-addListener(callback: (event: MediaQueryEvent) => void): void--><!--Device-MediaQueryList-addListener(callback: (event: MediaQueryEvent) => void): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event: MediaQueryEvent) =&gt; void | 是 |  |

## onchange

```TypeScript
onchange?: (matches: boolean) => void
```

Called when the matches value changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaQueryList-onchange?: (matches: boolean) => void--><!--Device-MediaQueryList-onchange?: (matches: boolean) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matches | boolean | 是 |  |

## removeListener

```TypeScript
removeListener(callback: (event: MediaQueryEvent) => void): void
```

Removes a listening function from MediaQueryList.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaQueryList-removeListener(callback: (event: MediaQueryEvent) => void): void--><!--Device-MediaQueryList-removeListener(callback: (event: MediaQueryEvent) => void): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | (event: MediaQueryEvent) =&gt; void | 是 |  |

## matches

```TypeScript
matches?: boolean
```

Whether the query is successful. True if the query condition is matched successfully, false otherwise.This parameter is read-only.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaQueryList-matches?: boolean--><!--Device-MediaQueryList-matches?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## media

```TypeScript
media?: string
```

Serialized media query condition.This parameter is read-only.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-MediaQueryList-media?: string--><!--Device-MediaQueryList-media?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

