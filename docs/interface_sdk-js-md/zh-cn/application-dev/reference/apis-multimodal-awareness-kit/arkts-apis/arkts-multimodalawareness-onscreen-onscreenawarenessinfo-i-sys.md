# OnscreenAwarenessInfo（系统接口）

Returns the list of onscreen awareness information.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-onScreen-export interface OnscreenAwarenessInfo--><!--Device-onScreen-export interface OnscreenAwarenessInfo-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## appIndex

```TypeScript
appIndex?: int
```

Application index.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-appIndex?: int--><!--Device-OnscreenAwarenessInfo-appIndex?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## appName

```TypeScript
appName?: string
```

Application name.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-appName?: string--><!--Device-OnscreenAwarenessInfo-appName?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## bundleName

```TypeScript
bundleName?: string
```

Application bundle name.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-bundleName?: string--><!--Device-OnscreenAwarenessInfo-bundleName?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## collectStrategy

```TypeScript
collectStrategy?: int
```

Page collection policy, which is the bitwise OR operation combination of &lt;br&gt; [CollectStrategy](arkts-multimodalawareness-onscreen-collectstrategy-e-sys.md).

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-collectStrategy?: int--><!--Device-OnscreenAwarenessInfo-collectStrategy?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## displayId

```TypeScript
displayId?: long
```

Display ID.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-displayId?: long--><!--Device-OnscreenAwarenessInfo-displayId?: long-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## entityInfo

```TypeScript
entityInfo?: EntityInfo[]
```

Entity information.

**类型：** [EntityInfo](arkts-multimodalawareness-onscreen-entityinfo-i-sys.md)[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-entityInfo?: EntityInfo[]--><!--Device-OnscreenAwarenessInfo-entityInfo?: EntityInfo[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## items

```TypeScript
items?: AwarenessItem[]
```

Data item information.

**类型：** [AwarenessItem](arkts-multimodalawareness-onscreen-awarenessitem-i-sys.md)[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-items?: AwarenessItem[]--><!--Device-OnscreenAwarenessInfo-items?: AwarenessItem[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## languageInfo

```TypeScript
languageInfo?: string
```

Page language information.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-languageInfo?: string--><!--Device-OnscreenAwarenessInfo-languageInfo?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## miniProgramId

```TypeScript
miniProgramId?: string
```

Applet ID, for example, the ID of WeChat or Alipay.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-miniProgramId?: string--><!--Device-OnscreenAwarenessInfo-miniProgramId?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## miniProgramName

```TypeScript
miniProgramName?: string
```

Name of a third-party mini program.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-miniProgramName?: string--><!--Device-OnscreenAwarenessInfo-miniProgramName?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## pageId

```TypeScript
pageId?: string
```

Application page ID.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-pageId?: string--><!--Device-OnscreenAwarenessInfo-pageId?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## pageTags

```TypeScript
pageTags?: string[]
```

Page tag information.

**类型：** string[]

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-pageTags?: string[]--><!--Device-OnscreenAwarenessInfo-pageTags?: string[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## resultCode

```TypeScript
resultCode: int
```

Return code. The default value **0** indicates success.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-resultCode: int--><!--Device-OnscreenAwarenessInfo-resultCode: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## sampleId

```TypeScript
sampleId?: string
```

Collection record ID.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-sampleId?: string--><!--Device-OnscreenAwarenessInfo-sampleId?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## timestamp

```TypeScript
timestamp: long
```

Timestamp for accessing a specified page, in milliseconds.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-timestamp: long--><!--Device-OnscreenAwarenessInfo-timestamp: long-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## uid

```TypeScript
uid?: string
```

Application UID.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-uid?: string--><!--Device-OnscreenAwarenessInfo-uid?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## windowId

```TypeScript
windowId?: int
```

Window ID.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-OnscreenAwarenessInfo-windowId?: int--><!--Device-OnscreenAwarenessInfo-windowId?: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

