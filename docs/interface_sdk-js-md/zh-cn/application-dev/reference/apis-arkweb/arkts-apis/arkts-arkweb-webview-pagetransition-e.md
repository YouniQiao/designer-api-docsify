# PageTransition

```TypeScript
enum PageTransition
```

页面跳转类型枚举。`PageTransition`值由两部分组成：

**核心类型**（低字节，取值 0–10）：表示主要的导航原因，如[LINK](#link)、[TYPED](#typed)、[FORM_SUBMIT](#form_submit)、[RELOAD](#reload)、[AUTO_SUBFRAME](#auto_subframe)等。每次导航有且仅有一个核心类型。

**修饰标志**（高位）：表示额外的导航特征，如[FORWARD_BACK](#forward_back)（前进/后退导航）、[FROM_API](#from_api)（API 触发）、[CLIENT_REDIRECT](#client_redirect)（JavaScript/meta 重定向）、[SERVER_REDIRECT](#server_redirect)（HTTP 重定向）等。一次导航可包含零个或多个修饰标志。

组合跳转值由核心类型与修饰标志按位或得到。可使用掩码常量进行拆解：`CORE_MASK`提取核心类型，`QUALIFIER_MASK`提取修饰标志，`IS_REDIRECT_MASK`判断是否包含重定向。

例如，`TYPED | FROM_ADDRESS_BAR`得到的组合值为`0x02000001`。使用`combined & CORE_MASK`（结果`0x01`）提取核心类型`TYPED`；使用`combined & QUALIFIER_MASK`（结果`0x02000000`）提取修饰标志`FROM_ADDRESS_BAR`；使用`(combined & FROM_ADDRESS_BAR) !== 0`判断是否由地址栏触发；使用`(combined & IS_REDIRECT_MASK) !== 0`判断是否包含重定向。

**起始版本：** 26.1.0

<!--Device-webview-enum PageTransition--><!--Device-webview-enum PageTransition-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## AUTO_SUBFRAME

```TypeScript
AUTO_SUBFRAME = 3
```

子帧导航。指在非顶层帧中自动加载的内容。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-AUTO_SUBFRAME = 3--><!--Device-PageTransition-AUTO_SUBFRAME = 3-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## AUTO_TOPLEVEL

```TypeScript
AUTO_TOPLEVEL = 6
```

顶层导航。指在顶层帧中自动加载的内容。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-AUTO_TOPLEVEL = 6--><!--Device-PageTransition-AUTO_TOPLEVEL = 6-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## CHAIN_END

```TypeScript
CHAIN_END = 0x20000000
```

重定向链中的最后一次跳转。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-CHAIN_END = 0x20000000--><!--Device-PageTransition-CHAIN_END = 0x20000000-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## CHAIN_START

```TypeScript
CHAIN_START = 0x10000000
```

导航链的起始。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-CHAIN_START = 0x10000000--><!--Device-PageTransition-CHAIN_START = 0x10000000-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## CLIENT_REDIRECT

```TypeScript
CLIENT_REDIRECT = 0x40000000
```

由 JavaScript 或页面 meta refresh 标签触发的重定向。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-CLIENT_REDIRECT = 0x40000000--><!--Device-PageTransition-CLIENT_REDIRECT = 0x40000000-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## CORE_MASK

```TypeScript
CORE_MASK = 0xFF
```

掩码，用于从组合跳转值中提取核心跳转类型。与组合跳转值按位与，结果为`PageTransition`核心类型枚举值。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-CORE_MASK = 0xFF--><!--Device-PageTransition-CORE_MASK = 0xFF-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## FORM_SUBMIT

```TypeScript
FORM_SUBMIT = 7
```

用户填写表单并提交。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-FORM_SUBMIT = 7--><!--Device-PageTransition-FORM_SUBMIT = 7-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## FORWARD_BACK

```TypeScript
FORWARD_BACK = 0x01000000
```

用户通过前进或后退按钮在浏览历史中导航。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-FORWARD_BACK = 0x01000000--><!--Device-PageTransition-FORWARD_BACK = 0x01000000-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## FROM_ADDRESS_BAR

```TypeScript
FROM_ADDRESS_BAR = 0x02000000
```

用户通过地址栏触发本次导航。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-FROM_ADDRESS_BAR = 0x02000000--><!--Device-PageTransition-FROM_ADDRESS_BAR = 0x02000000-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## FROM_API

```TypeScript
FROM_API = 0x08000000
```

跳转由 API 调用或外部应用发起。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-FROM_API = 0x08000000--><!--Device-PageTransition-FROM_API = 0x08000000-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## IS_REDIRECT_MASK

```TypeScript
IS_REDIRECT_MASK = -1073741824
```

掩码，用于判断跳转是否为重定向（客户端或服务端）。与组合跳转值按位与，结果非 0 表示导航包含重定向。该掩码由 [CLIENT_REDIRECT](#client_redirect) | [SERVER_REDIRECT](#server_redirect) 按位或得到。十六进制表示为 0xC0000000。因超出 int32 最大值，使用带符号十进制表示。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-IS_REDIRECT_MASK = -1073741824--><!--Device-PageTransition-IS_REDIRECT_MASK = -1073741824-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## LINK

```TypeScript
LINK = 0
```

用户通过点击其他页面上的链接跳转到本页面。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-LINK = 0--><!--Device-PageTransition-LINK = 0-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## MANUAL_SUBFRAME

```TypeScript
MANUAL_SUBFRAME = 4
```

用户显式请求的子帧导航，会在前进/后退列表中生成新的导航条目。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-MANUAL_SUBFRAME = 4--><!--Device-PageTransition-MANUAL_SUBFRAME = 4-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## QUALIFIER_MASK

```TypeScript
QUALIFIER_MASK = -256
```

掩码，用于从组合跳转值中提取修饰标志位。十六进制表示为 0xFFFFFF00。因超出 int32 最大值，使用带符号十进制表示。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-QUALIFIER_MASK = -256--><!--Device-PageTransition-QUALIFIER_MASK = -256-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## RELOAD

```TypeScript
RELOAD = 8
```

用户重新加载页面，可通过点击刷新按钮或在地址栏按回车触发。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-RELOAD = 8--><!--Device-PageTransition-RELOAD = 8-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## SERVER_REDIRECT

```TypeScript
SERVER_REDIRECT = -2147483648
```

由服务器通过 HTTP 头发送的重定向。十六进制表示为 0x80000000。因超出 int32 最大值，使用带符号十进制表示。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-SERVER_REDIRECT = -2147483648--><!--Device-PageTransition-SERVER_REDIRECT = -2147483648-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## TYPED

```TypeScript
TYPED = 1
```

用户在地址栏输入地址跳转到本页面。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PageTransition-TYPED = 1--><!--Device-PageTransition-TYPED = 1-End-->

**系统能力：** SystemCapability.Web.Webview.Core
