# input

Provides methods for setting information about input methods, including automatic capitalization, automatic punctuation, autocorrect, password presentation, input method engine, and input method subtypes.

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

<!--Device-settings-namespace input--><!--Device-settings-namespace input-End-->

**系统能力：** SystemCapability.Applications.Settings.Core

## 导入模块

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 常量

| 名称 | 说明 |
| --- | --- |
| [DEFAULT_INPUT_METHOD](arkts-basicservices-input-con.md#default_input_method) | Indicates the default input method and its ID. |
| [ACTIVATED_INPUT_METHOD_SUB_MODE](arkts-basicservices-input-con.md#activated_input_method_sub_mode) | Indicates the default input method keyboard type and its ID. |
| [ACTIVATED_INPUT_METHODS](arkts-basicservices-input-con.md#activated_input_methods) | Indicates the list of input methods that have been activated.  &lt;p&gt;The list is a string that contains the IDs of activated input methods. The IDs are separated by colons(:), and keyboardTypes of an input method are separated by semicolons (;). An example format is{@code ima0:keyboardType0;keyboardType1;ima1:ima2:keyboardTypes0}. The type of &lt;b&gt;imaID&lt;/b&gt; is ElementName,and the type of &lt;b&gt;keyboard&lt;/b&gt; is int. |
| [SELECTOR_VISIBILITY_FOR_INPUT_METHOD](arkts-basicservices-input-con.md#selector_visibility_for_input_method) | Specifies whether the input method selector is visible.  &lt;p&gt;If the value is {@code 1}, the input method selector is visible. If the value is {@code 0}, the input method selector is invisible. |
| [AUTO_CAPS_TEXT_INPUT](arkts-basicservices-input-con.md#auto_caps_text_input) | Specifies whether automatic capitalization is enabled for the text editor.  &lt;p&gt;If the value is {@code 0}, automatic capitalization is disabled. If the value {@code 1}, automatic capitalization is enabled. |
| [AUTO_PUNCTUATE_TEXT_INPUT](arkts-basicservices-input-con.md#auto_punctuate_text_input) | Specifies whether automatic punctuation is enabled for the text editor. Automatic punctuation enables the text editor to convert two spaces into a period (.) and a space.  &lt;p&gt;If the value is {@code 0}, automatic punctuation is disabled. If the value {@code 1}, automatic punctuation is enabled. |
| [AUTO_REPLACE_TEXT_INPUT](arkts-basicservices-input-con.md#auto_replace_text_input) | Specifies whether autocorrect is enabled for the text editor. Autocorrect enables the text editor to correct typos.  &lt;p&gt;If the value is {@code 0}, autocorrect is disabled. If the value {@code 1}, autocorrect is enabled. |
| [SHOW_PASSWORD_TEXT_INPUT](arkts-basicservices-input-con.md#show_password_text_input) | Specifies whether password presentation is enabled in the text editor. Password presentation enables the text editor to show password characters when the user types them.  &lt;p&gt;If the value is {@code 0}, password presentation is disabled. If the value {@code 1}, password presentation is enabled. |

