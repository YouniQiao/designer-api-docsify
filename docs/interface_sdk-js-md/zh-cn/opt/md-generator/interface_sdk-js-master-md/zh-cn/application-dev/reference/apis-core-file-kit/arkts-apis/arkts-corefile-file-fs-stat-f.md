# stat

## stat

```TypeScript
declare function stat(file: string | number): Promise<Stat>
```

获取文件或目录详细属性信息，使用promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function stat(file: string | number): Promise<Stat>--><!--Device-unnamed-declare function stat(file: string | number): Promise<Stat>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| file | string \| number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Stat&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |
| 13900011 |


## stat

```TypeScript
declare function stat(file: string | number, callback: AsyncCallback<Stat>): void
```

获取文件或目录的详细属性信息，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function stat(file: string | number, callback: AsyncCallback<Stat>): void--><!--Device-unnamed-declare function stat(file: string | number, callback: AsyncCallback<Stat>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| file | string \| number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Stat&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |
| 13900011 |
