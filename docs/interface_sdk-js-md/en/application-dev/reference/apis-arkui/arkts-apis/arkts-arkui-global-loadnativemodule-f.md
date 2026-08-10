# loadNativeModule

## loadNativeModule

```TypeScript
export declare function loadNativeModule(moduleName: string): Object
```

同步动态加载native模块，目的是按需加载所需要的模块。使用该接口会增加so文件的加载时间，使用前需评估其对应用性能和功能的影响。

> **说明：**
> 
> loadNativeModule加载的模块名称为依赖方oh-package.json5文件的dependencies字段中声明的依赖名称。
> 
> loadNativeModule仅支持在Stage模型的UI主线程中加载native模块。
> 
> 无论moduleName参数使用常量字符串还是变量表达式，都需要配置接口调用的依赖。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-export declare function loadNativeModule(moduleName: string): Object--><!--Device-unnamed-export declare function loadNativeModule(moduleName: string): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| moduleName | string | Yes | 加载的模块名。 |

**Return value:**

| Type | Description |
| --- | --- |
| Object | native模块的默认导出，需使用ArkTS的ESObject类型去接收。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | The parameter check failed. |
| 10200301 | Loading native module failed. |

