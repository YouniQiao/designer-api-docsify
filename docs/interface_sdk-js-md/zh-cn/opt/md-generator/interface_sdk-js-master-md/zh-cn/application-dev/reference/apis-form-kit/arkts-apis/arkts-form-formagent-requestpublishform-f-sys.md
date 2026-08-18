# requestPublishForm（系统接口）

## 导入模块

```TypeScript
```

## requestPublishForm

```TypeScript
function requestPublishForm(want: Want, callback: AsyncCallback<string>): void
```

请求发布一张卡片到使用方，使用callback异步回调。使用方通常为桌面。适用于系统应用需要主动将卡片添加到桌面的场景。

**起始版本：** 23

**需要权限：** ohos.permission.AGENT_REQUIRE_FORM

<!--Device-formAgent-function requestPublishForm(want: Want, callback: AsyncCallback<string>): void--><!--Device-formAgent-function requestPublishForm(want: Want, callback: AsyncCallback<string>): void-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501002](../errorcode-form.md#16501002-卡片数量达到上限) |
| 16501018 |
| 16501017 |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16501008](../errorcode-form.md#16501008-等待卡片加桌超时) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |


## requestPublishForm

```TypeScript
function requestPublishForm(want: Want): Promise<string>
```

请求发布一张卡片到使用方，使用Promise异步回调。使用方通常为桌面。适用于系统应用需要主动将卡片添加到桌面的场景。

**起始版本：** 23

**需要权限：** ohos.permission.AGENT_REQUIRE_FORM

<!--Device-formAgent-function requestPublishForm(want: Want): Promise<string>--><!--Device-formAgent-function requestPublishForm(want: Want): Promise<string>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16501002](../errorcode-form.md#16501002-卡片数量达到上限) |
| 16501018 |
| 16501017 |
| [16501000](../errorcode-form.md#16501000-内部功能错误) |
| [16500050](../errorcode-form.md#16500050-进程间通信失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [16501008](../errorcode-form.md#16501008-等待卡片加桌超时) |
| [16500100](../errorcode-form.md#16500100-获取卡片配置信息失败) |
