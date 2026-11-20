# inputmethod_types_capi.h

## Overview

Defines the types related to the input method.

**File to Include**: <inputmethod/inputmethod_types_capi.h>

**Library**: libohinputmethod.so

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

**Related module**: [InputMethod](capi-ime-kit-inputmethod.md)

## Summary

### Enums

| Name | typedef keyword | Description |
| -- | -- | -- |
| [InputMethod_KeyboardStatus](#inputmethod_keyboardstatus) | InputMethod_KeyboardStatus | Enumerates the keyboard status. |
| [InputMethod_EnterKeyType](#inputmethod_enterkeytype) | InputMethod_EnterKeyType | Enumerates the Enter key types. |
| [InputMethod_Direction](#inputmethod_direction) | InputMethod_Direction | Enumerates the moving directions. |
| [InputMethod_ExtendAction](#inputmethod_extendaction) | InputMethod_ExtendAction | Enumerates the types of the extended edit action on the text box. |
| [InputMethod_TextInputType](#inputmethod_textinputtype) | InputMethod_TextInputType | Enumerates the text input types. |
| [InputMethod_CommandValueType](#inputmethod_commandvaluetype) | InputMethod_CommandValueType | Enumerates the private data types. |
| [InputMethod_ErrorCode](#inputmethod_errorcode) | InputMethod_ErrorCode | Enumeration of error codes of the input method, which defines the error codes that may occur in the input method framework, covering various error scenarios such as parameter check failure, package management exception, input method application exception, and text box client exception. Developers need to determine the error type based on the specific error code and take corresponding measures to rectify the error. For details, see [Input Method Framework Error Codes](errorcode-inputmethod-framework.md). <br> <br>Function: Identifies the execution results and error types of various operations in the input method framework, which is used to determine interface return values and handle errors. <br> <br>Suggested value: After invoking the input method C API, check whether the return value is IME_ERR_OK(0). If a value other than IME_ERR_OK is returned, rectify the fault based on the error code: IME_ERR_NULL_POINTER checks whether the parameter value is NULL. IME_ERR_PARAMCHECK checks the parameter type and range. The IME_ERR_IMCLIENT/IME_ERR_DETACHED checks the connection between the input box and the input method service. IME_ERR_IMENGINE checks the running status of the input method application. IME_ERR_QUERY_FAILED checks the query conditions and data status. <br> <br> Relationship between enumerated values: Enumerated values are classified into three groups: common error codes(0, 1, 401), framework service error codes(12800001-12800029), and C API error codes(12802000-12802001). Common error codes are applicable to all interfaces. Framework service error codes are related to system service status. Error codes dedicated to C APIs apply to null pointers and query failure scenarios specific to C language interfaces. IME_ERR_OK(0) indicates success, and other values indicate error. |
| [InputMethod_RequestKeyboardReason](#inputmethod_requestkeyboardreason) | InputMethod_RequestKeyboardReason | Enumerates the reasons for requesting the keyboard. |
| [OH_InputMethod_UnderlineStyle](#oh_inputmethod_underlinestyle) | OH_InputMethod_UnderlineStyle | Pre-screen text underline style enumeration. |
| [OH_InputMethod_InputCapabilityType](#oh_inputmethod_inputcapabilitytype) | OH_InputMethod_InputCapabilityType | Input capability type enumeration. |

### Macros

| Name | Description |
| -- | -- |
| OHOS_INPUTMETHOD_TYPES_CAPI_H | Defines the types related to the input method.<br>**Since**: 12<br>**System capability**: SystemCapability.MiscServices.InputMethodFramework |

## Enum type description

### InputMethod_KeyboardStatus

```c
enum InputMethod_KeyboardStatus
```

**Description**

Enumerates the keyboard status.

<!--Device-InputMethod_KeyboardStatus--><!--Device-InputMethod_KeyboardStatus-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

| Enum item | Description |
| -- | -- |
| IME_KEYBOARD_STATUS_NONE = 0 | NONE. |
| IME_KEYBOARD_STATUS_HIDE = 1 | Invisible. |
| IME_KEYBOARD_STATUS_SHOW = 2 | Visible. |

### InputMethod_EnterKeyType

```c
enum InputMethod_EnterKeyType
```

**Description**

Enumerates the Enter key types.

<!--Device-InputMethod_EnterKeyType--><!--Device-InputMethod_EnterKeyType-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

| Enum item | Description |
| -- | -- |
| IME_ENTER_KEY_UNSPECIFIED = 0 | Unspecified. |
| IME_ENTER_KEY_NONE = 1 | NONE. |
| IME_ENTER_KEY_GO = 2 | Go. |
| IME_ENTER_KEY_SEARCH = 3 | Search. |
| IME_ENTER_KEY_SEND = 4 | Send. |
| IME_ENTER_KEY_NEXT = 5 | Next. |
| IME_ENTER_KEY_DONE = 6 | Done. |
| IME_ENTER_KEY_PREVIOUS = 7 | Previous. |
| IME_ENTER_KEY_NEWLINE = 8 | Line break. |

### InputMethod_Direction

```c
enum InputMethod_Direction
```

**Description**

Enumerates the moving directions.

<!--Device-InputMethod_Direction--><!--Device-InputMethod_Direction-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

| Enum item | Description |
| -- | -- |
| IME_DIRECTION_NONE = 0 | NONE. |
| IME_DIRECTION_UP = 1 | Upward. |
| IME_DIRECTION_DOWN = 2 | Downward. |
| IME_DIRECTION_LEFT = 3 | Leftward. |
| IME_DIRECTION_RIGHT = 4 | Rightward. |

### InputMethod_ExtendAction

```c
enum InputMethod_ExtendAction
```

**Description**

Enumerates the types of the extended edit action on the text box.

<!--Device-InputMethod_ExtendAction--><!--Device-InputMethod_ExtendAction-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

| Enum item | Description |
| -- | -- |
| IME_EXTEND_ACTION_SELECT_ALL = 0 | Select all. |
| IME_EXTEND_ACTION_CUT = 3 | Cut. |
| IME_EXTEND_ACTION_COPY = 4 | Copy. |
| IME_EXTEND_ACTION_PASTE = 5 | Paste. |

### InputMethod_TextInputType

```c
enum InputMethod_TextInputType
```

**Description**

Enumerates the text input types.

<!--Device-InputMethod_TextInputType--><!--Device-InputMethod_TextInputType-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

| Enum item | Description |
| -- | -- |
| IME_TEXT_INPUT_TYPE_NONE = -1 | NONE. |
| IME_TEXT_INPUT_TYPE_TEXT = 0 | Text. |
| IME_TEXT_INPUT_TYPE_MULTILINE = 1 | Multi-line. |
| IME_TEXT_INPUT_TYPE_NUMBER = 2 | Number. |
| IME_TEXT_INPUT_TYPE_PHONE = 3 | Phone number. |
| IME_TEXT_INPUT_TYPE_DATETIME = 4 | Date. |
| IME_TEXT_INPUT_TYPE_EMAIL_ADDRESS = 5 | Email address. |
| IME_TEXT_INPUT_TYPE_URL = 6 | URL. |
| IME_TEXT_INPUT_TYPE_VISIBLE_PASSWORD = 7 | Password. |
| IME_TEXT_INPUT_TYPE_NUMBER_PASSWORD = 8 | Numeric password. |
| IME_TEXT_INPUT_TYPE_SCREEN_LOCK_PASSWORD = 9 | Lock screen password. |
| IME_TEXT_INPUT_TYPE_USER_NAME = 10 | Username. |
| IME_TEXT_INPUT_TYPE_NEW_PASSWORD = 11 | New password. |
| IME_TEXT_INPUT_TYPE_NUMBER_DECIMAL = 12 | Decimal number. |
| IME_TEXT_INPUT_TYPE_ONE_TIME_CODE = 13 | Verification code.<br>**Since**: 20 |

### InputMethod_CommandValueType

```c
enum InputMethod_CommandValueType
```

**Description**

Enumerates the private data types.

<!--Device-InputMethod_CommandValueType--><!--Device-InputMethod_CommandValueType-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

| Enum item | Description |
| -- | -- |
| IME_COMMAND_VALUE_TYPE_NONE = 0 | NONE. |
| IME_COMMAND_VALUE_TYPE_STRING = 1 | String. |
| IME_COMMAND_VALUE_TYPE_BOOL = 2 | Boolean. |
| IME_COMMAND_VALUE_TYPE_INT32 = 3 | 32-bit signed integer. |

### InputMethod_ErrorCode

```c
enum InputMethod_ErrorCode
```

**Description**

Enumeration of error codes of the input method, which defines the error codes that may occur in the input method framework, covering various error scenarios such as parameter check failure, package management exception, input method application exception, and text box client exception. Developers need to determine the error type based on the specific error code and take corresponding measures to rectify the error. For details, see [Input Method Framework Error Codes](errorcode-inputmethod-framework.md). <br> <br>Function: Identifies the execution results and error types of various operations in the input method framework, which is used to determine interface return values and handle errors. <br> <br>Suggested value: After invoking the input method C API, check whether the return value is IME_ERR_OK(0). If a value other than IME_ERR_OK is returned, rectify the fault based on the error code: IME_ERR_NULL_POINTER checks whether the parameter value is NULL. IME_ERR_PARAMCHECK checks the parameter type and range. The IME_ERR_IMCLIENT/IME_ERR_DETACHED checks the connection between the input box and the input method service. IME_ERR_IMENGINE checks the running status of the input method application. IME_ERR_QUERY_FAILED checks the query conditions and data status. <br> <br> Relationship between enumerated values: Enumerated values are classified into three groups: common error codes(0, 1, 401), framework service error codes(12800001-12800029), and C API error codes(12802000-12802001). Common error codes are applicable to all interfaces. Framework service error codes are related to system service status. Error codes dedicated to C APIs apply to null pointers and query failure scenarios specific to C language interfaces. IME_ERR_OK(0) indicates success, and other values indicate error.

<!--Device-InputMethod_ErrorCode--><!--Device-InputMethod_ErrorCode-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 12

| Enum item | Description |
| -- | -- |
| IME_ERR_OK = 0 | &nbsp;Success. |
| IME_ERR_UNDEFINED = 1 | &nbsp;Undefined error. |
| IME_ERR_PARAMCHECK = 401 | &nbsp;Parameter check failed. |
| IME_ERR_PACKAGEMANAGER = 12800001 | &nbsp;Package management error. |
| IME_ERR_IMENGINE = 12800002 | &nbsp;Input method application error. |
| IME_ERR_IMCLIENT = 12800003 | &nbsp;Text box client error. |
| IME_ERR_CONFIG_PERSIST = 12800005 | &nbsp;Configuration persistence failed. This error code is reported when the configuration fails to be saved. |
| IME_ERR_CONTROLLER = 12800006 | &nbsp;Input method controller error. |
| IME_ERR_SETTINGS = 12800007 | &nbsp;Input method setter error. |
| IME_ERR_IMMS = 12800008 | &nbsp;Input method manager service error. |
| IME_ERR_DETACHED = 12800009 | &nbsp;Text box unbound. |
| OH_INPUTMETHOD_ERR_NOT_DEFAULT_IME = 12800010 | Error code when the current input method is not the default input method preset in the system.<br>**Since**: 26.1.0 |
| OH_INPUTMETHOD_ERR_EDITABLE = 12800016 | The text box is in the non-editing state. The text box may still be bound. This error cannot be equated with unbound.<br>**Since**: 26.1.0 |
| OH_INPUTMETHOD_ERR_INPUT_CAPABILITY_TYPE_NOT_SUPPORTED = 12800029 | Error code when the input capability type is not supported.<br>**Since**: 26.1.0 |
| IME_ERR_NULL_POINTER = 12802000 | &nbsp;Null pointer. |
| IME_ERR_QUERY_FAILED = 12802001 | &nbsp;Query failed. |

### InputMethod_RequestKeyboardReason

```c
enum InputMethod_RequestKeyboardReason
```

**Description**

Enumerates the reasons for requesting the keyboard.

<!--Device-InputMethod_RequestKeyboardReason--><!--Device-InputMethod_RequestKeyboardReason-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 15

| Enum item | Description |
| -- | -- |
| IME_REQUEST_REASON_NONE = 0 | No reason. |
| IME_REQUEST_REASON_MOUSE = 1 | Mouse operation. |
| IME_REQUEST_REASON_TOUCH = 2 | Touch operation. |
| IME_REQUEST_REASON_OTHER = 20 | Other reasons. |

### OH_InputMethod_UnderlineStyle

```c
enum OH_InputMethod_UnderlineStyle
```

**Description**

Pre-screen text underline style enumeration.

<!--Device-OH_InputMethod_UnderlineStyle--><!--Device-OH_InputMethod_UnderlineStyle-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 26.1.0

| Enum item | Description |
| -- | -- |
| OH_INPUTMETHOD_UNDERLINE_STYLE_NONE = 0 | No underline.<br>**Since**: 26.1.0 |
| OH_INPUTMETHOD_UNDERLINE_STYLE_SOLID = 1 | Solid underline.<br>**Since**: 26.1.0 |
| OH_INPUTMETHOD_UNDERLINE_STYLE_WAVY = 2 | Wavy lines underline.<br>**Since**: 26.1.0 |
| OH_INPUTMETHOD_UNDERLINE_STYLE_DASHED = 3 | Dotted underline.<br>**Since**: 26.1.0 |

### OH_InputMethod_InputCapabilityType

```c
enum OH_InputMethod_InputCapabilityType
```

**Description**

Input capability type enumeration.

<!--Device-OH_InputMethod_InputCapabilityType--><!--Device-OH_InputMethod_InputCapabilityType-End-->

**System capability**: SystemCapability.MiscServices.InputMethodFramework

**Since**: 26.1.0

| Enum item | Description |
| -- | -- |
| OH_INPUTMETHOD_INPUT_CAPABILITY_TYPE_TRANSLATION = 0 | Set Capability Type to Translation.<br>**Since**: 26.1.0 |


