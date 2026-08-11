# copyDir

## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, mode?: number): Promise<void>
```

复制源目录至目标路径下，使用promise异步回调。

**起始版本：** 10

<!--Device-unnamed-declare function copyDir(src: string, dest: string, mode?: number): Promise<void>--><!--Device-unnamed-declare function copyDir(src: string, dest: string, mode?: number): Promise<void>-End-->

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


## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, callback: AsyncCallback<void>): void
```

复制源目录至目标路径下，使用callback异步回调。

**起始版本：** 10

<!--Device-unnamed-declare function copyDir(src: string, dest: string, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyDir(src: string, dest: string, callback: AsyncCallback<void>): void-End-->

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


## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void
```

复制源目录至目标路径下，使用callback异步回调。

如果目标目录下有与源目录名冲突的目录，且冲突目录下有同名文件，则抛出异常。源目录下未冲突的文件全部移动至目标目录下，目标目录下未冲突文件将继续保留，且冲突文件信息将在抛出异常的data属性中以Array\&lt;  
[ConflictFiles](arkts-corefile-file-fs-conflictfiles-i.md)&gt;形式提供。

**起始版本：** 10

<!--Device-unnamed-declare function copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void--><!--Device-unnamed-declare function copyDir(src: string, dest: string, callback: AsyncCallback<void, Array<ConflictFiles>>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| dest | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;ConflictFiles&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900015 |


## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void
```

复制源目录至目标路径下，可设置复制模式。使用callback异步回调。

**起始版本：** 10

<!--Device-unnamed-declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void--><!--Device-unnamed-declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void>): void-End-->

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


## copyDir

```TypeScript
declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void
```

复制源目录至目标路径下，可设置复制模式。使用callback异步回调。

**起始版本：** 10

<!--Device-unnamed-declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void--><!--Device-unnamed-declare function copyDir(src: string, dest: string, mode: number, callback: AsyncCallback<void, Array<ConflictFiles>>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | string | 是 |
| dest | string | 是 |
| mode | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void, Array&lt;ConflictFiles&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900015 |
