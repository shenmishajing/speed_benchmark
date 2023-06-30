## Introduction

A generic speed benchmark library. It runs every func with every arg to get the average time cost and also checks the result.

The `funcs` parameter is a `dict` of function name and functions to evaluate. The `args` parameter is a `dict` with key `main_arg_name` and `data`. The `main_arg_name` is used to determine the variable name of each group argument of the function, and the `data` is a dict of `<main_arg_value>:<args_of_func>`. The `data` can also be a list of arguments. If so, the `main_arg_name` must be in each group of arguments and the value of it will be used as the `main_arg_value`.

Also, you can set the `pre_func`, `post_func`, and `check_result_func` to change the behavior of the benchmark.
