# PageTransition

```TypeScript
enum PageTransition
```

Enumerates the page transition types. The `PageTransition` value consists of two parts:

**Core type** (low byte, values 0–10): Represents the primary navigation cause, such as [LINK](#link), [TYPED](#typed), [FORM_SUBMIT](#form_submit), [RELOAD](#reload), [AUTO_SUBFRAME](#auto_subframe), etc. Each navigation has exactly one core type.

**Qualifier flags** (high bits): Represent additional navigation characteristics, such as [FORWARD_BACK](#forward_back) (back/forward navigation), [FROM_API](#from_api) (API-triggered), [CLIENT_REDIRECT](#client_redirect) (JavaScript/meta redirect), [SERVER_REDIRECT](#server_redirect) (HTTP redirect), etc. A navigation can have zero or more qualifier flags.

A combined transition value is formed by OR'ing a core type with qualifier flags. Use the mask constants to decompose it: `CORE_MASK` extracts the core type, `QUALIFIER_MASK` extracts the qualifier flags, and `IS_REDIRECT_MASK` checks whether the navigation involves a redirect.

For example, `TYPED | FROM_ADDRESS_BAR` produces a combined value of `0x02000001`. Use `combined & CORE_MASK` (result: `0x01`) to extract the core type `TYPED`; use `combined & QUALIFIER_MASK` (result: `0x02000000`) to extract the qualifier `FROM_ADDRESS_BAR`; use `(combined & FROM_ADDRESS_BAR) !== 0` to check whether the navigation was triggered from the address bar; use `(combined & IS_REDIRECT_MASK) !== 0` to check whether the navigation involves a redirect.

**Since:** 26.1.0

<!--Device-webview-enum PageTransition--><!--Device-webview-enum PageTransition-End-->

**System capability:** SystemCapability.Web.Webview.Core

## AUTO_SUBFRAME

```TypeScript
AUTO_SUBFRAME = 3
```

This is a subframe navigation. This is any content that is automatically loaded in a non-toplevel frame.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-AUTO_SUBFRAME = 3--><!--Device-PageTransition-AUTO_SUBFRAME = 3-End-->

**System capability:** SystemCapability.Web.Webview.Core

## AUTO_TOPLEVEL

```TypeScript
AUTO_TOPLEVEL = 6
```

This is a toplevel navigation. This is any content that is automatically loaded in a toplevel frame.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-AUTO_TOPLEVEL = 6--><!--Device-PageTransition-AUTO_TOPLEVEL = 6-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CHAIN_END

```TypeScript
CHAIN_END = 0x20000000
```

The last transition in a redirect chain.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-CHAIN_END = 0x20000000--><!--Device-PageTransition-CHAIN_END = 0x20000000-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CHAIN_START

```TypeScript
CHAIN_START = 0x10000000
```

The beginning of a navigation chain.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-CHAIN_START = 0x10000000--><!--Device-PageTransition-CHAIN_START = 0x10000000-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CLIENT_REDIRECT

```TypeScript
CLIENT_REDIRECT = 0x40000000
```

Redirects caused by JavaScript or a meta refresh tag on the page.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-CLIENT_REDIRECT = 0x40000000--><!--Device-PageTransition-CLIENT_REDIRECT = 0x40000000-End-->

**System capability:** SystemCapability.Web.Webview.Core

## CORE_MASK

```TypeScript
CORE_MASK = 0xFF
```

Mask to extract the core page transition type from a combined transition value. Use bitwise AND with a combined transition value; the result is a `PageTransition` core type enum value.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-CORE_MASK = 0xFF--><!--Device-PageTransition-CORE_MASK = 0xFF-End-->

**System capability:** SystemCapability.Web.Webview.Core

## FORM_SUBMIT

```TypeScript
FORM_SUBMIT = 7
```

The user filled out values in a form and submitted it.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-FORM_SUBMIT = 7--><!--Device-PageTransition-FORM_SUBMIT = 7-End-->

**System capability:** SystemCapability.Web.Webview.Core

## FORWARD_BACK

```TypeScript
FORWARD_BACK = 0x01000000
```

The user used the Forward or Back button to navigate among browsing history.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-FORWARD_BACK = 0x01000000--><!--Device-PageTransition-FORWARD_BACK = 0x01000000-End-->

**System capability:** SystemCapability.Web.Webview.Core

## FROM_ADDRESS_BAR

```TypeScript
FROM_ADDRESS_BAR = 0x02000000
```

The user used the address bar to trigger this navigation.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-FROM_ADDRESS_BAR = 0x02000000--><!--Device-PageTransition-FROM_ADDRESS_BAR = 0x02000000-End-->

**System capability:** SystemCapability.Web.Webview.Core

## FROM_API

```TypeScript
FROM_API = 0x08000000
```

The transition originated from an API call or an external application.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-FROM_API = 0x08000000--><!--Device-PageTransition-FROM_API = 0x08000000-End-->

**System capability:** SystemCapability.Web.Webview.Core

## IS_REDIRECT_MASK

```TypeScript
IS_REDIRECT_MASK = -1073741824
```

Mask, which is used to determine whether a redirection is a redirection(client or server). The combined jump value is bitwise ANDed with, and the result is a non-zero result indicating that the navigation contains redirection. The mask is obtained by the bitwise OR of [CLIENT_REDIRECT](#client_redirect) | [SERVER_REDIRECT](#server_redirect). The value is 0xC0000000 in hexadecimal notation. The value is expressed in signed decimal notation because it exceeds the maximum value of int32.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-IS_REDIRECT_MASK = -1073741824--><!--Device-PageTransition-IS_REDIRECT_MASK = -1073741824-End-->

**System capability:** SystemCapability.Web.Webview.Core

## LINK

```TypeScript
LINK = 0
```

The user navigated to this page by clicking a link on another page.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-LINK = 0--><!--Device-PageTransition-LINK = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## MANUAL_SUBFRAME

```TypeScript
MANUAL_SUBFRAME = 4
```

The user explicitly requested a subframe navigation that generates new navigation entries in the back/forward list.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-MANUAL_SUBFRAME = 4--><!--Device-PageTransition-MANUAL_SUBFRAME = 4-End-->

**System capability:** SystemCapability.Web.Webview.Core

## QUALIFIER_MASK

```TypeScript
QUALIFIER_MASK = -256
```

mask used to extract the modifier flag bits from the combined jump value. The value is 0xFFFFFF00 in hexadecimal notation. The value is expressed in signed decimal notation because it exceeds the maximum value of int32.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-QUALIFIER_MASK = -256--><!--Device-PageTransition-QUALIFIER_MASK = -256-End-->

**System capability:** SystemCapability.Web.Webview.Core

## RELOAD

```TypeScript
RELOAD = 8
```

The user reloaded the page, either by pressing the reload button or by pressing Enter in the address bar.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-RELOAD = 8--><!--Device-PageTransition-RELOAD = 8-End-->

**System capability:** SystemCapability.Web.Webview.Core

## SERVER_REDIRECT

```TypeScript
SERVER_REDIRECT = -2147483648
```

Redirection sent by the server via HTTP header. The value is 0x80000000 in hexadecimal notation. The value is expressed in signed decimal notation because it exceeds the maximum value of int32.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-SERVER_REDIRECT = -2147483648--><!--Device-PageTransition-SERVER_REDIRECT = -2147483648-End-->

**System capability:** SystemCapability.Web.Webview.Core

## TYPED

```TypeScript
TYPED = 1
```

The user navigated to this page by typing the address in the URL bar.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-PageTransition-TYPED = 1--><!--Device-PageTransition-TYPED = 1-End-->

**System capability:** SystemCapability.Web.Webview.Core
