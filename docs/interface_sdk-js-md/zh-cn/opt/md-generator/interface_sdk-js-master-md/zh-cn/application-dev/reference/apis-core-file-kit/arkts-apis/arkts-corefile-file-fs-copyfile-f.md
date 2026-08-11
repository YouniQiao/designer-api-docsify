# copyFile

## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>
```

复制文件，使用promise异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>--><!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string \| number | 是 |
| dest | string \| number | 是 |
| mode | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900018 |
| 13900019 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900034 |
| 13900012 |
| 13900044 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |
| 13900011 |


## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void
```

复制文件，覆盖方式为完全覆盖目标文件，未覆盖部分将被裁切。使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string \| number | 是 |
| dest | string \| number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900018 |
| 13900019 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900034 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |
| 13900011 |


## copyFile

```TypeScript
declare function copyFile(
  src: string | number,
  dest: string | number,
  mode: number,
  callback: AsyncCallback<void>
): void
```

复制文件，可设置覆盖文件的方式，使用callback异步回调。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare function copyFile(  src: string | number,  dest: string | number,  mode: number,  callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyFile(  src: string | number,  dest: string | number,  mode: number,  callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string \| number | 是 |
| dest | string \| number | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900018 |
| 13900019 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900034 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900010 |
| 13900042 |
| 13900011 |
