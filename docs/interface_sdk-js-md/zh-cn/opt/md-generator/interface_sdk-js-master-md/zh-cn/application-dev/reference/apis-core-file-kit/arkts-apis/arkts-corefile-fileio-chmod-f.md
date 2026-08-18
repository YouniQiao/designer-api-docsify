# chmod

## 导入模块

```TypeScript
```

## chmod

```TypeScript
declare function chmod(path: string, mode: number): Promise<void>
```

改变文件权限，使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

<!--Device-unnamed-declare function chmod(path: string, mode: number): Promise<void>--><!--Device-unnamed-declare function chmod(path: string, mode: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## chmod

```TypeScript
declare function chmod(path: string, mode: number, callback: AsyncCallback<void>): void
```

改变文件权限，使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

<!--Device-unnamed-declare function chmod(path: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function chmod(path: string, mode: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |
