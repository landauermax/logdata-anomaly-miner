# skipcq: PYL-W0104
{
    'Analysis': {
        'required': False,
        'type': 'list',
        'nullable': True,
        'schema': {
            'type': 'dict',
            'schema': {
                'id': {'type': 'string', 'nullable': True, 'default': None},
                'type': {'type': 'analysistype', 'coerce': 'toanalysistype', 'required': True},
                'paths': {'type': 'list', 'schema': {'type': 'string'}, 'nullable': True, 'default': None},
                'labels': {'type': 'list', 'schema': {'type': 'string'}, 'nullable': True, 'default': None},
                'persistence_id': {'type': 'string', 'default': 'Default'},
                'output_logline': {'type': 'boolean', 'default': True},
                'learn_mode': {'type': 'boolean'},
                'allow_missing_values': {'type': 'boolean', 'default': False},
                'check_interval': {'type': 'integer', 'default': 3600},
                'realert_interval': {'type': 'integer', 'default': 36000},
                'report_interval': {'type': 'integer', 'default': 10},
                'reset_after_report_flag': {'type': 'boolean', 'default': False},
                'path': {'type': 'string', 'default': 'Default'},
                'parallel_check_count': {'type': 'integer', 'required': True, 'default': 10},
                'record_count_before_event': {'type': 'integer', 'default': 1000},
                'use_path_match': {'type': 'boolean', 'default': True},
                'use_value_match': {'type': 'boolean', 'default': True},
                'min_rule_attributes': {'type': 'integer', 'default': 1},
                'max_rule_attributes': {'type': 'integer', 'default': 5},
                'max_hypotheses': {'type': 'integer', 'default': 1000},
                'hypothesis_max_delta_time': {'type': 'float', 'default': 5.0},
                'generation_probability': {'type': 'float', 'default': 1.0},
                'generation_factor': {'type': 'float', 'default': 1.0},
                'max_observations': {'type': 'integer', 'default': 500},
                'p0': {'type': 'float', 'default': 0.9},
                'alpha': {'type': 'float', 'default': 0.05},
                'candidates_size': {'type': 'integer', 'default': 10},
                'hypotheses_eval_delta_time': {'type': 'float', 'default': 120.0},
                'delta_time_to_discard_hypothesis': {'type': 'float', 'default': 180.0},
                'check_rules_flag': {'type': 'boolean', 'default': True},
                'constraint_list': {
                    'type': 'list', 'schema': {'type': 'string'}, 'nullable': True, 'default': None},
                'ignore_list': {
                    'type': 'list', 'schema': {'type': 'string'}, 'nullable': True, 'default': None},
                'id_path_list': {'type': 'list', 'default': []},
                'seq_len': {'type': 'integer', 'default': 3},
                'window_size': {'type': ['integer', 'float'], 'default': 600},
                'confidence_factor': {'type': 'float', 'default': 0.5},
                'min_allowed_time_diff': {'type': 'float', 'default': 5.0},
                'lower_limit': {'type': ['integer', 'float']},
                'upper_limit': {'type': ['integer', 'float']},
                'bin_size': {'type': 'integer'},
                'bin_count': {'type': 'integer'},
                'outlier_bins_flag': {'type': 'boolean', 'default': False},
                'modulo_value': {'type': 'integer'},
                'time_unit': {'type': 'integer'},
                'histogram_defs': {'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'string'}}},
                'bin_definition': {'type': 'string'},
                'tuple_transformation_function': {'type': 'string', 'allowed': ['demo'], 'nullable': True, 'default': None},
                'value_list': {
                    'type': 'list', 'schema': {'type': ['boolean', 'float', 'integer', 'string']}, 'nullable': True, 'default': None},
                'timestamp_path': {'type': 'string'},
                'min_bin_elements': {'type': 'integer'},
                'min_bin_time': {'type': 'integer'},
                'debug_mode': {'type': 'boolean', 'default': False},
                # skipcq: PYL-W0511
                # TODO check which streams should be allowed
                'stream': {'type': 'string', 'allowed': ['sys.stdout', 'sys.stderr']},
                'separator': {'type': 'string'},
                'missing_value_string': {'type': 'string'},
                'event_type': {'type': 'string'},
                'event_message': {'type': 'string'},
                'stop_when_handled_flag': {'type': 'boolean', 'default': False},
                'sub_rules': {'type': 'list', 'schema': {'type': 'string'}},
                'sub_rule': {'type': 'string'},
                'match_action': {'type': 'string', 'nullable': True, 'default': None},
                'rule_lookup_dict': {'type': 'dict', 'schema': {'id': {'type': 'string'}, 'type': {'type': 'string'}}},
                'default_rule': {'type': 'string', 'nullable': True, 'default': None},
                'value': {'type': ['boolean', 'float', 'integer', 'string']},
                'regex': {'type': 'string'},
                'seconds_modulo': {'type': 'integer'},
                'limit_lookup_dict': {
                    'type': 'dict', 'schema': {'id': {'type': 'string'}, 'type': {'type': 'list', 'schema': {'type': 'integer'}}}},
                'default_limit': {'type': 'list', 'schema': {'type': 'integer'}, 'nullable': True, 'default': None},
                'rule_id': {'type': 'string'},
                'min_time_delta': {'type': 'integer'},
                'max_time_delta': {'type': 'integer'},
                'max_artefacts_a_for_single_b': {'type': 'integer'},
                'artefact_match_parameters': {'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'string'}},
                                              'nullable': True, 'default': None},
                'action_id': {'type': 'string'},
                'artefact_a_rules': {'type': 'list', 'schema': {'type': 'string'}, 'nullable': True, 'default': None},
                'artefact_b_rules': {'type': 'list', 'schema': {'type': 'string'}, 'nullable': True, 'default': None},
                'ruleset': {'type': 'list', 'schema': {'type': 'string'}},
                'exit_on_error_flag': {'type': 'boolean', 'default': False},
                'allowlist_rules': {'type': 'list', 'schema': {'type': 'string'}},
                'parsed_atom_handler_lookup_list': {
                    'type': 'list', 'schema': {'type': 'list', 'schema': {'type': 'string', 'nullable': True}}},
                'default_parsed_atom_handler': {'type': 'string', 'nullable': True, 'default': None},
                'parsed_atom_handler_dict': {'type': 'dict', 'schema': {'id': {'type': 'string'}, 'type': {'type': 'string'}}},
                'min_num_vals': {'type': 'integer', 'default': 1000},
                'max_num_vals': {'type': 'integer', 'default': 1500},
                'save_values': {'type': 'boolean', 'default': True},
                'track_time_for_TSA': {'type': 'boolean', 'default': False},
                'waiting_time_for_TSA': {'type': 'integer', 'default': 300},
                'num_sections_waiting_time_for_TSA': {'type': 'integer', 'default': 10},
                'event_type_detector': {'type': 'string'},
                'ks_alpha': {'type': 'float', 'default': 0.05},
                's_ks_alpha': {'type': 'float', 'default': 0.05},
                's_ks_bt_alpha': {'type': 'float', 'default': 0.05},
                'd_alpha': {'type': 'float', 'default': 0.1},
                'd_bt_alpha': {'type': 'float', 'default': 0.1},
                'div_thres': {'type': 'float', 'default': 0.3},
                'sim_thres': {'type': 'float', 'default': 0.1},
                'indicator_thres': {'type': 'float', 'default': 0.4},
                'num_init': {'type': 'integer', 'default': 100},
                'num_update': {'type': 'integer', 'default': 50},
                'num_update_unq': {'type': 'integer', 'default': 200},
                'num_s_ks_values': {'type': 'integer', 'default': 50},
                'num_s_ks_bt': {'type': 'integer', 'default': 30},
                'num_d_bt': {'type': 'integer', 'default': 30},
                'num_pause_discrete': {'type': 'integer', 'default': 5},
                'num_pause_others': {'type': 'integer', 'default': 2},
                'test_ks_int': {'type': 'boolean', 'default': True},
                'update_var_type_bool': {'type': 'boolean', 'default': True},
                'num_stop_update': {'type': 'boolean', 'default': False},
                'silence_output_without_confidence': {'type': 'boolean', 'default': False},
                'silence_output_except_indicator': {'type': 'boolean', 'default': True},
                'num_var_type_hist_ref': {'type': 'integer', 'default': 10},
                'num_update_var_type_hist_ref': {'type': 'integer', 'default': 10},
                'num_var_type_considered_ind': {'type': 'integer', 'default': 10},
                'num_stat_stop_update': {'type': 'integer', 'default': 200},
                'num_updates_until_var_reduction': {'type': 'integer', 'default': 20},
                'var_reduction_thres': {'type': 'float', 'default': 0.6},
                'num_skipped_ind_for_weights': {'type': 'integer', 'default': 1},
                'num_ind_for_weights': {'type': 'integer', 'default': 100},
                'used_multinomial_test': {'type': 'string', 'allowed': ['Approx', 'MT', 'Chi'], 'default': 'Chi'},
                'use_empiric_distr': {'type': 'boolean', 'default': True},
                'save_statistics': {'type': 'boolean', 'default': True},
                'split_reports_flag': {'type': 'boolean', 'default': False},
                'disc_div_thres': {'type': 'float', 'default': 0.3},
                'num_steps_create_new_rules': {'type': 'integer', 'default': -1},
                'num_upd_until_validation': {'type': 'integer', 'default': 20},
                'num_end_learning_phase': {'type': 'integer', 'default': -1},
                'check_cor_thres': {'type': 'float', 'default': 0.5},
                'check_cor_prob_thres': {'type': 'float', 'default': 1.0},
                'check_cor_num_thres': {'type': 'integer', 'default': 10},
                'min_values_cors_thres': {'type': 'integer', 'default': 5},
                'new_vals_alarm_thres': {'type': 'float', 'default': 3.5},
                'num_bt': {'type': 'integer', 'default': 30},
                'alpha_bt': {'type': 'float', 'default': 0.1},
                'used_homogeneity_test': {'type': 'string', 'allowed': ['Chi', 'MaxDist'], 'default': 'Chi'},
                'alpha_chisquare_test': {'type': 'float', 'default': 0.05},
                'max_dist_rule_distr': {'type': 'float', 'default': 0.1},
                'used_presel_meth': {'type': 'list', 'schema': {'type': 'string', 'allowed': [
                    'matchDiscDistr', 'excludeDueDistr', 'matchDiscVals', 'random']}, 'nullable': True, 'default': None},
                'intersect_presel_meth': {'type': 'boolean', 'default': False},
                'percentage_random_cors': {'type': 'float', 'default': 0.20},
                'match_disc_vals_sim_tresh': {'type': 'float', 'default': 0.7},
                'exclude_due_distr_lower_limit': {'type': 'float', 'default': 0.4},
                'match_disc_distr_threshold': {'type': 'float', 'default': 0.5},
                'used_cor_meth': {'type': 'list', 'schema': {'type': 'string', 'allowed': ['Rel', 'WRel']},
                                  'nullable': True, 'default': None},
                'used_validate_cor_meth': {'type': 'list', 'schema': {'type': 'string', 'allowed': [
                    'coverVals', 'distinctDistr']}, 'nullable': True, 'default': None},
                'validate_cor_cover_vals_thres': {'type': 'float', 'default': 0.7},
                'validate_cor_distinct_thres': {'type': 'float', 'default': 0.05},
                'output_event_handlers': {'type': 'list', 'nullable': True, 'default': None},
                'suppress': {'type': 'boolean', 'default': False}
            }
        }
    }
}