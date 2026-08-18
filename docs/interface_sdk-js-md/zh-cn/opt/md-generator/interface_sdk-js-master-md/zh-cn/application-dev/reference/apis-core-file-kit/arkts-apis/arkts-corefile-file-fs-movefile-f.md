# moveFile

## 导入模块

```TypeScript
```

## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, mode?: number): Promise<void>
```

移动文件，使用promise异步回调。 > **说明：** > > 该接口不支持在分布式文件路径下操作。

**起始版本：** 9

<!--Device-unnamed-declare function moveFile(src: string, dest: string, mode?: number): Promise<void>--><!--Device-unnamed-declare function moveFile(src: string, dest: string, mode?: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| dest | string | 是 |
| mode | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900025 |
| 13900027 |
| 13900032 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |


## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, callback: AsyncCallback<void>): void
```

移动文件。如果移动位置存在同名文件，将强制覆盖。使用callback异步回调。 > **说明：** > > 该接口不支持在分布式文件路径下操作。

**起始版本：** 9

<!--Device-unnamed-declare function moveFile(src: string, dest: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function moveFile(src: string, dest: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| dest | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900025 |
| 13900027 |
| 13900032 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |


## moveFile

```TypeScript
declare function moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void
```

移动文件，支持设置移动模式。使用callback异步回调。 > **说明：** > > 该接口不支持在分布式文件路径下操作。

**起始版本：** 9

<!--Device-unnamed-declare function moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function moveFile(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| dest | string | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900016 |
| 13900018 |
| 13900019 |
| 13900028 |
| 13900025 |
| 13900027 |
| 13900032 |
| 13900001 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900014 |
| 13900015 |
| 13900008 |
| 13900041 |
| 13900042 |
| 13900011 |
