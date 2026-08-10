# AwarenessItem（系统接口）

Provides page information, which includes:

* Basic page information, such as page content, links, and screenshots.  
* Page entity information, such as the title and body of a page article.  
* Page interaction information, such as clicks and scrolling.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-onScreen-export interface AwarenessItem--><!--Device-onScreen-export interface AwarenessItem-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## itemInfo

```TypeScript
itemInfo: Record<string, Object>
```

Entity information of the awareness result, including the content, links, screenshots, and other entity information.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-AwarenessItem-itemInfo: Record<string, Object>--><!--Device-AwarenessItem-itemInfo: Record<string, Object>-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

