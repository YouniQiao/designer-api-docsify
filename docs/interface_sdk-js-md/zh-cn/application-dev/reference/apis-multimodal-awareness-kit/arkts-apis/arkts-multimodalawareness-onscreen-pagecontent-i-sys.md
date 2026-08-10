# PageContent（系统接口）

Defines the onscreen content.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-onScreen-export interface PageContent--><!--Device-onScreen-export interface PageContent-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the onscreen content.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PageContent-bundleName: string--><!--Device-PageContent-bundleName: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## content

```TypeScript
content?: string
```

Body of the onscreen content. This parameter is available only when **options.contentUnderstand** is set to   
**True**.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PageContent-content?: string--><!--Device-PageContent-content?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## pageLink

```TypeScript
pageLink?: string
```

Page link of the onscreen content. This parameter is available only when **options.pageLink** is set to **True**.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PageContent-pageLink?: string--><!--Device-PageContent-pageLink?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## paragraphs

```TypeScript
paragraphs?: Paragraph[]
```

Paragraph information of the onscreen content. This parameter is available only when **options.textOnly** is set to **True**.

**类型：** [Paragraph](../../apis-arkui/arkts-apis/arkts-arkui-paragraph-t.md)[]

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PageContent-paragraphs?: Paragraph[]--><!--Device-PageContent-paragraphs?: Paragraph[]-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## scenario

```TypeScript
scenario?: Scenario
```

Scenario of the onscreen content. This parameter is available only when **options.contentUnderstand** is set to   
**True**.

**类型：** [Scenario](arkts-multimodalawareness-onscreen-scenario-e-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PageContent-scenario?: Scenario--><!--Device-PageContent-scenario?: Scenario-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## sessionId

```TypeScript
sessionId: long
```

Session ID, which identifies the call action.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PageContent-sessionId: long--><!--Device-PageContent-sessionId: long-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## title

```TypeScript
title?: string
```

Title of the onscreen content. This parameter is available only when **options.contentUnderstand** is set to   
**True**.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PageContent-title?: string--><!--Device-PageContent-title?: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## windowId

```TypeScript
windowId: int
```

Window ID of the onscreen content.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-PageContent-windowId: int--><!--Device-PageContent-windowId: int-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

