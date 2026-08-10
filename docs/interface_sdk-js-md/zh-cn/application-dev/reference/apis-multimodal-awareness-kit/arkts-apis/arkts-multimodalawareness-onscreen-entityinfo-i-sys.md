# EntityInfo（系统接口）

Provides entity information perceived, including content, links, images, and other types of entities.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-onScreen-export interface EntityInfo--><!--Device-onScreen-export interface EntityInfo-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { onScreen } from 'kits/@kit.MultimodalAwarenessKit';
```

## entityInfo

```TypeScript
entityInfo: Record<string, Object>
```

Entity information of the awareness result, including the content, links, images, and other entity information.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EntityInfo-entityInfo: Record<string, Object>--><!--Device-EntityInfo-entityInfo: Record<string, Object>-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

## entityName

```TypeScript
entityName: string
```

Name of the perceived entity, which is fixed.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-EntityInfo-entityName: string--><!--Device-EntityInfo-entityName: string-End-->

**系统能力：** SystemCapability.MultimodalAwareness.OnScreenAwareness

**系统接口：** 此接口为系统接口。

