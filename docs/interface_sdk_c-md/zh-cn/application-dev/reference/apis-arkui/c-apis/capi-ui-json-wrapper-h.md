# ui_json_wrapper.h

## 概述

Declares the shared JSON data object for the UI perception and control APIs.

**引用文件：** <arkui/ui_json_wrapper.h>

**库：** libace_ndk.z.so

**起始版本：** 26.2.0

**相关模块：** [ArkUI_NativeModule](capi-arkui-nativemodule.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| -- | -- | -- |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) | OH_ArkUI_NativeModule_UIJsonWrapper | 定义一个不透明、不可变的JSON数据对象。<br> 对象拥有一个UTF-8 JSON字符串以及该字符串的模式版本 JSON，它既用于框架传递的数据（UI感知），也用于 应用程序（UI控件）提交的命令。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| -- | -- | -- |
| [OH_ArkUI_NativeModule_UIJsonFormat](#oh_arkui_nativemodule_uijsonformat) | OH_ArkUI_NativeModule_UIJsonFormat | JSON输出格式枚举类型。 |

### 函数

| 名称 | 描述 |
| -- | -- |
| [ArkUI_ErrorCode OH_ArkUI_NativeModule_UIJsonWrapperCreate(const char *data, uint32_t size, OH_ArkUI_NativeModule_UIJsonWrapper **outOwned)](#oh_arkui_nativemodule_uijsonwrappercreate) | 从调用方提供的JSON字符串创建JSON数据对象。<br> 将提供的字符串复制到对象中。调用方拥有创建的对象，必须 当不再需要它时，使用[OH_ArkUI_NativeModule_UIJsonWrapperDestroy](capi-ui-json-wrapper-h.md#oh_arkui_nativemodule_uijsonwrapperdestroy)释放它。<br> 提供的字符串应包含schemaVersion字段。如果不存在，或指定的 版本值超出支持的范围，它被视为1，如下所示： { "schemaVersion": 1, ... }<br> 注意：传递给此函数的数据字符串仍由调用方拥有。销毁JSON 此接口返回的包装器对象不会释放数据指向的内存 调用者的代表。 |
| [const char *OH_ArkUI_NativeModule_UIJsonWrapperGetData(const OH_ArkUI_NativeModule_UIJsonWrapper *json)](#oh_arkui_nativemodule_uijsonwrappergetdata) | 获取对象持有的JSON字符串。<br> 返回的字符串是只读的，并且以null终止。它指向JSON拥有的内存 对象，并保持有效，直到对象被销毁。调用者不得修改或释放 返回的字符串。 |
| [uint32_t OH_ArkUI_NativeModule_UIJsonWrapperGetSize(const OH_ArkUI_NativeModule_UIJsonWrapper *json)](#oh_arkui_nativemodule_uijsonwrappergetsize) | 获取JSON字符串的字节长度。<br> 返回的长度不包括终止空字符。对于一个空的JSON字符串，零是 返回。 |
| [void OH_ArkUI_NativeModule_UIJsonWrapperDestroy(OH_ArkUI_NativeModule_UIJsonWrapper *json)](#oh_arkui_nativemodule_uijsonwrapperdestroy) | 销毁JSON数据对象并释放其资源。<br> 传递null没有任何效果。返回的任何指针 OH_ArkUI_NativeModule_UIJsonWrapper_GetData在此次调用后失效。<br> 注意：仅在您显式持有其所有权的JSON包装器对象上调用此函数，对于 例如，使用OH_ArkUI_NativeModule_UIJsonWrapper_Create创建的包装器，或者包装器 你通过所有权转移函数明确地获得了所有权。不使用 该函数用于释放系统构造并传递出去的JSON包装器对象。 例如，通过传递的对象 [OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectioninteractionjsoncallback)。 |

## 枚举类型说明

### OH_ArkUI_NativeModule_UIJsonFormat

```c
enum OH_ArkUI_NativeModule_UIJsonFormat
```

**描述：**

JSON输出格式枚举类型。

**起始版本：** 26.2.0

| 枚举项 | 描述 |
| -- | -- |
| OH_ARKUI_NATIVE_MODULE_UI_JSON_COMPACT = 0 | 生成规范的JSON，没有不必要的空白。<br>**起始版本：** 26.2.0 |
| OH_ARKUI_NATIVE_MODULE_UI_JSON_PRETTY = 1 | 生成带有双空格缩进和换行符的JSON。<br>**起始版本：** 26.2.0 |


## 函数说明

### OH_ArkUI_NativeModule_UIJsonWrapperCreate()

```c
ArkUI_ErrorCode OH_ArkUI_NativeModule_UIJsonWrapperCreate(const char *data, uint32_t size, OH_ArkUI_NativeModule_UIJsonWrapper **outOwned)
```

**描述：**

从调用方提供的JSON字符串创建JSON数据对象。<br> 将提供的字符串复制到对象中。调用方拥有创建的对象，必须 当不再需要它时，使用[OH_ArkUI_NativeModule_UIJsonWrapperDestroy](capi-ui-json-wrapper-h.md#oh_arkui_nativemodule_uijsonwrapperdestroy)释放它。<br> 提供的字符串应包含schemaVersion字段。如果不存在，或指定的 版本值超出支持的范围，它被视为1，如下所示： { "schemaVersion": 1, ... }<br> 注意：传递给此函数的数据字符串仍由调用方拥有。销毁JSON 此接口返回的包装器对象不会释放数据指向的内存 调用者的代表。

**起始版本：** 26.2.0

**资源释放：** ui_json_wrapper/OH_ArkUI_NativeModule_UIJsonWrapperDestroy {outOwned}

**参数：**

| 参数项 | 描述 |
| -- | -- |
| const char *data | [in] 指向JSON字符串的指针。它不能为空，并且必须对 呼叫的持续时间。被调用方不保留。空字符串是有效的，对应 的大小为0。 |
| uint32_t size | [in] JSON字符串的字节长度，单位为字节，不包括终止null。 字符，必须等于数据的实际长度。如果大小与实际不一致 返回字符串长度ARKUI_ERROR_CODE_PARAM_INVALID。 |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) **outOwned | [out] 成功时接收创建的对象。调用方拥有返回的对象 并且必须使用[OH_ArkUI_NativeModule_UIJsonWrapperDestroy](capi-ui-json-wrapper-h.md#oh_arkui_nativemodule_uijsonwrapperdestroy)来释放它。一定不是这样的 null，不需要初始化，失败时设置为null。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| [ArkUI_ErrorCode](capi-error-code-h.md#arkui_errorcode) | <ul> <li>ARKUI_ERROR_CODE_NO_ERROR 如果操作成功。</li> <li>ARKUI_ERROR_CODE_PARAM_INVALID 如果参数无效。</li> </ul> |

### OH_ArkUI_NativeModule_UIJsonWrapperGetData()

```c
const char *OH_ArkUI_NativeModule_UIJsonWrapperGetData(const OH_ArkUI_NativeModule_UIJsonWrapper *json)
```

**描述：**

获取对象持有的JSON字符串。<br> 返回的字符串是只读的，并且以null终止。它指向JSON拥有的内存 对象，并保持有效，直到对象被销毁。调用者不得修改或释放 返回的字符串。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) *json | [in] JSON数据对象。不能为空。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| const char * | 借用的JSON字符串，如果json为null，则为null。 |

### OH_ArkUI_NativeModule_UIJsonWrapperGetSize()

```c
uint32_t OH_ArkUI_NativeModule_UIJsonWrapperGetSize(const OH_ArkUI_NativeModule_UIJsonWrapper *json)
```

**描述：**

获取JSON字符串的字节长度。<br> 返回的长度不包括终止空字符。对于一个空的JSON字符串，零是 返回。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [const OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) *json | [in] JSON数据对象。不能为空。 |

**返回值：**

| 类型 | 说明 |
| -- | -- |
| uint32_t | <ul> <li>JSON字符串的字节长度，不包括终止空字符。</li> <li>对于空的JSON字符串返回0。</li> </ul> |

### OH_ArkUI_NativeModule_UIJsonWrapperDestroy()

```c
void OH_ArkUI_NativeModule_UIJsonWrapperDestroy(OH_ArkUI_NativeModule_UIJsonWrapper *json)
```

**描述：**

销毁JSON数据对象并释放其资源。<br> 传递null没有任何效果。返回的任何指针 OH_ArkUI_NativeModule_UIJsonWrapper_GetData在此次调用后失效。<br> 注意：仅在您显式持有其所有权的JSON包装器对象上调用此函数，对于 例如，使用OH_ArkUI_NativeModule_UIJsonWrapper_Create创建的包装器，或者包装器 你通过所有权转移函数明确地获得了所有权。不使用 该函数用于释放系统构造并传递出去的JSON包装器对象。 例如，通过传递的对象 [OH_ArkUI_NativeModule_UIInfoCollectionInteractionJsonCallback](capi-ui-info-collection-h.md#oh_arkui_nativemodule_uiinfocollectioninteractionjsoncallback)。

**起始版本：** 26.2.0

**参数：**

| 参数项 | 描述 |
| -- | -- |
| [OH_ArkUI_NativeModule_UIJsonWrapper](capi-arkui-nativemodule-oh-arkui-nativemodule-uijsonwrapper.md) *json | [in] 要销毁的JSON数据对象。 |


