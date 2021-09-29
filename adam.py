def do_adam():

	w_b_dw_db = [ ( init_w, init_b, 0.0 ) ]
	
	w_history, b_history , error_history = [], [] , []
	
	w ,b ,eta, mini_batch_size, num_points_seen = init_w, init_b, 0.1, 10, 0
	
	
	for i in range(max_epochs):
		dw, db = 0, 0
		for x, y in zip(X,Y):
			dw + = grad_w(w,b,x,y)
			db+ = grad_b(w,b,x,y)
			
		m_w = beta1* m_v + (1-beta1) *dw
		m_b = beta1*m_b +(1-beta1)*db
		
		v_w = beta2* v_w +(1-beta2) *dw**2
		v_b = beta2* v_b + (1-beta2) *db**2
		
		m_w = m_w/(1-math.pow(beta1,i+1))
		m_b = m_b/(1-math.pow(beta1,i+1))
		
		v_w = v_w/(1-math.pow(beta2,i+1))
		v_b = v_b/(1-math.pow(beta2,i+1))
		
		w = w- (eta/np.sqrt(v_w+eps)) *m_v
		b = b-(eta/np.sqrt(v_b+eps))*m_b
		
