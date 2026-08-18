# KnowledgeContent（系统接口）

支持的MIME类型。

**起始版本：** 23

<!--Device-photoAccessHelper-class KnowledgeContent--><!--Device-photoAccessHelper-class KnowledgeContent-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
```

## getRelatedEntity

```TypeScript
static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>
```

返回Smartlabel推荐标签

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-KnowledgeContent-static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>--><!--Device-KnowledgeContent-static getRelatedEntity (topic: string, context: ContextMap, option?: Options): Promise<Entity[]>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| topic | string | 是 |
| context | [ContextMap](arkts-medialibrary-photoaccesshelper-contextmap-i-sys.md) | 是 |
| option | [Options](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-zlib-options-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Entity[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## getSearchResult

```TypeScript
static getSearchResult(query: SearchQuery): Promise<SearchResult>
```

根据提供的查询搜索媒资。该接口使用promise返回结果。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-KnowledgeContent-static getSearchResult(query: SearchQuery): Promise<SearchResult>--><!--Device-KnowledgeContent-static getSearchResult(query: SearchQuery): Promise<SearchResult>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| query | [SearchQuery](arkts-medialibrary-photoaccesshelper-searchquery-i-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;SearchResult & gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |

## getSearchSuggestion

```TypeScript
static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>
```

获取搜索推荐词

**起始版本：** 26.0.0

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-KnowledgeContent-static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>--><!--Device-KnowledgeContent-static getSearchSuggestion( searchSuggestionTypes: Array<SearchSuggestionType>): Promise<Array<SearchSuggestionResult>>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchSuggestionTypes | Array&lt;[SearchSuggestionType](arkts-medialibrary-photoaccesshelper-searchsuggestiontype-e-sys.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[SearchSuggestionResult](arkts-medialibrary-photoaccesshelper-searchsuggestionresult-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [23800301](../errorcode-medialibrary.md#23800301-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [23800151](../errorcode-medialibrary.md#23800151-场景参数校验不通过) |
