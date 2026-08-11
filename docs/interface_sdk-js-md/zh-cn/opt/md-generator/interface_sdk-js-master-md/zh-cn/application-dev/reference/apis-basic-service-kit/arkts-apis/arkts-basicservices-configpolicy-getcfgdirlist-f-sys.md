# getCfgDirList（系统接口）

## getCfgDirList

```TypeScript
function getCfgDirList(callback: AsyncCallback<Array<string>>): void
```

获取配置层级目录列表，按优先级从低到高。使用callback异步回调。

**起始版本：** 8

<!--Device-configPolicy-function getCfgDirList(callback: AsyncCallback<Array<string>>): void--><!--Device-configPolicy-function getCfgDirList(callback: AsyncCallback<Array<string>>): void-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |


## getCfgDirList

```TypeScript
function getCfgDirList(): Promise<Array<string>>
```

获取配置层级目录列表，按优先级从低到高。使用Promise异步回调。

**起始版本：** 8

<!--Device-configPolicy-function getCfgDirList(): Promise<Array<string>>--><!--Device-configPolicy-function getCfgDirList(): Promise<Array<string>>-End-->

**系统能力：** SystemCapability.Customization.ConfigPolicy

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;string&gt;&gt; |
