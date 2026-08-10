# KnowledgeContent（系统接口）

Knowledge Content class, used for geting related entity.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-photoAccessHelper-class KnowledgeContent--><!--Device-photoAccessHelper-class KnowledgeContent-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## getRelatedEntity

```TypeScript
static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>
```

Get Related Entities, Smart Label

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-KnowledgeContent-static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>--><!--Device-KnowledgeContent-static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| topic | string | 是 | Searching topic string. |
| context | [ContextMap](arkts-medialibrary-photoaccesshelper-contextmap-i-sys.md) | 是 | Context Map indicates topic filed. |
| option | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 | Options for getRelatedEntity. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Entity[]&gt; | Returns Array of Related Entities |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 13900020 | Parameter error. Possible causes: &lt;br&gt;1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by nonsystem application |

## getSearchSuggestion

```TypeScript
static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>
```

Get Search Suggestion.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-KnowledgeContent-static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>--><!--Device-KnowledgeContent-static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchSuggestionTypes | Array&lt;SearchSuggestionType&gt; | 是 | Array of search suggestion types &lt;br&gt;The maximum length is 7 and cannot be empty. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Array&lt;SearchSuggestionResult&gt;&gt; | Result of searching for recommended words |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 23800301 | Internal system error. It is recommended to retry and check the logs. &lt;br&gt;Possible causes: &lt;br&gt;1. Database corrupted; &lt;br&gt;2. The file system is abnormal; &lt;br&gt;3. The IPC request timed out. |
| 201 | Permission denied |
| 202 | Called by nonsystem application |
| 23800151 | Scenario parameters fail to pass the verification.Possible causes: &lt;br&gt;1. The searchSuggestionTypes list is empty. &lt;br&gt;2. The searchSuggestionTypes error. |

